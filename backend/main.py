from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DETAILS = os.getenv("MONGO_DETAILS")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

client = AsyncIOMotorClient(MONGO_DETAILS)
db = client.techstash_db
users_collection = db.users
cards_collection = db.cards

class CardCreate(BaseModel):
    title: str
    description: str
    link: str
    tags: list[str] = []

class UserAuth(BaseModel):
    email: EmailStr
    password: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# --- JWT ---
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# --- HELPER ---
def card_helper(card) -> dict:
    return {
        "id": str(card["_id"]),
        "title": card.get("title", ""),
        "description": card.get("description", ""),
        "link": card.get("link", ""),
        "tags": card.get("tags", []),
        "created_at": card.get("created_at")
    }

# --- ROUTES ---
@app.get("/")
async def root():
    return {"message": "API працює, змінні з .env підвантажені"}

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
    return {"message": "Реєстрація успішна"}

@app.post("/api/login")
async def login(user: UserAuth):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not pwd_context.verify(user.password, db_user["password_hash"]):
        raise HTTPException(status_code=401, detail="Невірний email або пароль")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/cards")
async def get_cards():
    cards = []
    async for document in cards_collection.find({}):
        cards.append(card_helper(document))
    return cards

@app.post("/api/cards")
async def add_card(card: CardCreate):
    new_card = {
        "title": card.title,
        "description": card.description,
        "link": card.link,
        "tags": card.tags,
        "created_at": datetime.utcnow()
    }

    result = await cards_collection.insert_one(new_card)
    created_card = await cards_collection.find_one({"_id": result.inserted_id})
    return card_helper(created_card)

@app.delete("/api/cards/{card_id}")
async def delete_card(card_id: str):
    result = await cards_collection.delete_one({"_id": ObjectId(card_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Картка не знайдена")

    return {"message": "Картка видалена", "id": card_id}

# --- ЗАПУСК ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
