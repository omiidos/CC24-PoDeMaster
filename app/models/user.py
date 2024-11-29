# app/models/user.py
from typing import Dict
from pydantic import BaseModel
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Constants for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory user DB (as a dictionary)
fake_users_db: Dict[str, "UserInDB"] = {}  

class User(BaseModel):
    username: str

class UserCreate(User):
    password: str

class UserInDB(User):
    hashed_password: str
    user_id: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Hash password function
def get_password_hash(password: str):
    return pwd_context.hash(password)

# Verify password function
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# JWT token generation function
def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt