import jwt
from datetime import datetime, timedelta
from src.app.config.config import settings
def create_tokens(user_id: str):
    # Дані, які ми зашиваємо в токен (payload)
    payload = {"sub": user_id}

    # Access Token
    access_expire = datetime.utcnow() + timedelta(minutes=30)
    access_token = jwt.encode(
        {**payload, "exp": access_expire},
        settings.JWT_SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    refresh_expire = datetime.utcnow() + timedelta(days=7)
    refresh_token = jwt.encode(
        {**payload, "exp": refresh_expire},
        settings.JWT_SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return access_token, refresh_token