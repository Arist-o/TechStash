import jwt
from fastapi import FastAPI, HTTPException, status, Depends, Body
from fastapi.security import OAuth2PasswordBearer
from bson import ObjectId
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.app.config.config import settings
from src.app.db.Database import get_user_collection
from src.app.db.UserModel import UserCreate, UserOut, UserUpdate, UserLogin, Role
from src.app.db.PasswordHasher import hash_password, verify_password
from src.app.db.AccessRefreshTokenGenerator import create_tokens
from src.app.db.UserModel import Token
from typing import List
app = FastAPI()
users_collection = get_user_collection()
security = HTTPBearer()

@app.post("/register", response_model=UserOut,tags=["Auth"])  # Обов'язково вкажи response_model
async def register(user_data: UserCreate):
    # 1. Перевіряємо, чи є такий юзер
    existing_user = await users_collection.find_one({"email": user_data.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Користувач з такою поштою вже існує"
        )

    # 2. Хешуємо пароль
    hashed_pwd = hash_password(user_data.password)

    # Створюємо документ для бази
    new_user_doc = {
        "email": user_data.email,
        "username": user_data.username,
        "password": hashed_pwd
    }

    # 3. Зберігаємо в MongoDB
    result = await users_collection.insert_one(new_user_doc)

    # 4. Готуємо дані для відповіді
    # Додаємо ID, який згенерувала MongoDB, конвертуючи його в рядок
    new_user_doc["_id"] = str(result.inserted_id)

    # ПЕРЕКОНАЙСЯ: ми повертаємо об'єкт, де є _id, email та username.
    # Pydantic сам відфільтрує 'password', бо його немає в моделі UserOut.
    return new_user_doc


@app.post("/login", response_model=Token, tags=["Auth"])
async def login(user_data: UserLogin):  # Повертаємо нашу JSON-модель
    # Тепер знову звертаємось через крапку до полів моделі
    user = await users_collection.find_one({"email": user_data.email})

    if not user:
        raise HTTPException(status_code=400, detail="Невірний email або пароль")

    if not verify_password(user_data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Невірний email або пароль")

    # Генеруємо токени
    access, refresh = create_tokens(str(user["_id"]))

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer"
    }




@app.post("/refresh", tags=["Auth"])
async def refresh_token_endpoint(refresh_token: str = Body(..., embed=True)):
    try:
        # 1. Декодуємо refresh токен
        payload = jwt.decode(refresh_token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Невалідний refresh токен")

        # 2. Можна додати перевірку в базі, чи такий юзер ще існує
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=401, detail="Користувача не знайдено")

        # 3. Генеруємо НОВУ пару токенів (Access + Refresh)
        new_access, new_refresh = create_tokens(str(user["_id"]))

        return {
            "access_token": new_access,
            "refresh_token": new_refresh,
            "token_type": "bearer"
        }
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Refresh токен прострочений або невалідний")
@app.get("/users", response_model=List[UserOut], tags=["Users"])
async def get_all_users():
    users = []
    # Шукаємо всіх користувачів (порожній {})
    async for user in users_collection.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return users


@app.get("/users/{user_id}", response_model=UserOut, tags=["Users"])
async def get_user_by_id(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Невірний формат ID")

    user = await users_collection.find_one({"_id": ObjectId(user_id)})

    if not user:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    user["_id"] = str(user["_id"])
    return user


async def get_current_user(auth: HTTPAuthorizationCredentials = Depends(security)):
    token = auth.credentials  # Отримуємо чистий токен
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Невалідний токен")

        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=401, detail="Користувача не знайдено")
        return user
    except Exception:
        raise HTTPException(status_code=401, detail="Помилка авторизації")

# Функція-перевірка на Адміна
def require_admin(current_user: dict = Depends(get_current_user)):
    if current_user.get("role") != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Ця дія доступна тільки для адміністраторів"
        )
    return current_user

@app.delete("/users/{user_id}", tags=["Users"])
async def delete_user(
        user_id: str,
        current_admin: dict = Depends(require_admin)  # Охорона тут!
):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Невірний формат ID")

    delete_result = await users_collection.delete_one({"_id": ObjectId(user_id)})

    if delete_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    return {"message": f"Користувача {user_id} успішно видалено адміном"}


@app.patch("/users/{user_id}", response_model=UserOut, tags=["Users"])
async def update_user(user_id: str, update_data: UserUpdate):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(status_code=400, detail="Невірний формат ID")

    # 1. Перетворюємо дані у словник
    update_dict = update_data.model_dump(exclude_unset=True)

    if not update_dict:
        raise HTTPException(status_code=400, detail="Не надано даних для оновлення")

    # 2. ЯКЩО В ДАНИХ Є ПАРОЛЬ — ХЕШУЄМО ЙОГО
    if "password" in update_dict:
        update_dict["password"] = hash_password(update_dict["password"])

    # 3. Оновлюємо в базі
    updated_user = await users_collection.find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": update_dict},
        return_document=True
    )

    if not updated_user:
        raise HTTPException(status_code=404, detail="Користувача не знайдено")

    # 4. Конвертуємо _id для Pydantic
    updated_user["_id"] = str(updated_user["_id"])
    return updated_user



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)