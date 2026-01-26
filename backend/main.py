from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from bson import ObjectId  # <-- ДОДАЙ ЦЕЙ ІМПОРТ

# --- КОНФІГУРАЦІЯ ПІДКЛЮЧЕННЯ ---
MONGO_DETAILS = "mongodb+srv://MARETU:Termin887ator@clustermar.blwfjzn.mongodb.net/?retryWrites=true&w=majority&appName=ClusterMar"

SECRET_KEY = "tech_stash_super_secret_key_2026"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.techstash_db
users_collection = db.users
cards_collection = db.cards

class CardCreate(BaseModel):
    title: str
    description: str
    link: str
    tags: list[str] = []

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserAuth(BaseModel):
    email: EmailStr
    password: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- МАРШРУТИ ---

@app.get("/")
async def root():
    return {"message": "API працює, підключення до Atlas встановлено"}

@app.post("/api/register")
async def register(user: UserAuth):
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Користувач вже існує")
    
    new_user = {
        "email": user.email,
        "password_hash": pwd_context.hash(user.password),
        "created_at": datetime.utcnow()
    }
    
    await users_collection.insert_one(new_user)
    return {"message": "Реєстрація успішна, дані в Atlas"}

@app.post("/api/login")
async def login(user: UserAuth):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not pwd_context.verify(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Невірний email або пароль")
    
    token = create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/cards")
async def get_cards():
    cards = []
    cursor = cards_collection.find({})
    async for document in cursor:
        document["id"] = str(document["_id"])  # <-- ЗМІНЕНО: використовуй "id" замість "_id"
        del document["_id"]  # Видаляємо _id, бо він не серіалізується
        cards.append(document)
    return cards

@app.post("/api/cards")
async def add_card(card: CardCreate):
    new_card = card.dict()
    new_card["created_at"] = datetime.utcnow()
    result = await cards_collection.insert_one(new_card)
    new_card["id"] = str(result.inserted_id)  # <-- ЗМІНЕНО: "id" замість "_id"
    return new_card

# --- НОВИЙ МАРШРУТ: ВИДАЛЕННЯ КАРТКИ ---
@app.delete("/api/cards/{card_id}")
async def delete_card(card_id: str):
    try:
        # Перетворюємо string ID на ObjectId MongoDB
        result = await cards_collection.delete_one({"_id": ObjectId(card_id)})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Картка не знайдена")
        
        return {"message": "Картка успішно видалена", "id": card_id}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Помилка: {str(e)}")


# --- ЗАПУСК СЕРВЕРА ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)