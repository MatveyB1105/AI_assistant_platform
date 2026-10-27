from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
# TODO: Добавить passlib и jwt для реальной аутентификации

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

class MockUser:
    def __init__(self, user_id: int, email: str, role: str):
        self.id = user_id
        self.email = email
        self.role = role

async def get_current_user(token: str = Depends(oauth2_scheme)) -> MockUser:
    # TODO: Реальная декодировка JWT токена и поиск пользователя в БД
    # Для демонстрации возвращаем мокового пользователя с ролью
    return MockUser(user_id=1, email="test@example.com", role="analyst")