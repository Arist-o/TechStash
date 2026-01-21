import os
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    MONGODB_URL: str = os.getenv("MONGODB_URL")
    DB_NAME: str = os.getenv("DB_NAME")

    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")  # Можна вказати дефолтне значення


settings = Settings()