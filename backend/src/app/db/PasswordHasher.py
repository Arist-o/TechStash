import bcrypt

def hash_password(password: str) -> str:
    # Перетворюємо рядок у байти
    pwd_bytes = password.encode('utf-8')
    # Генеруємо сіль
    salt = bcrypt.gensalt()
    # Хешуємо
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    # Повертаємо як рядок для збереження в БД
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Порівнюємо вхідний пароль із хешем із бази
    return bcrypt.checkpw(
        plain_password.encode('utf-8'),
        hashed_password.encode('utf-8')
    )