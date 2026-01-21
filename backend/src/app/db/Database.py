from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]

# Функція для отримання колекції користувачів
def get_user_collection():
    return db["users"]