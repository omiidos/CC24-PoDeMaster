from app.models.user import UserCreate, UserInDB, fake_users_db
from app.models.user import get_password_hash, verify_password, create_access_token
from typing import Optional
from datetime import timedelta
import uuid

fake_users_db = {}

# Create a new user in the system
async def create_user(user: UserCreate) -> UserInDB:
    """
    Create a new user in the system.
    """
    if user.username in fake_users_db:
        raise ValueError("Username already registered")
    hashed_password = get_password_hash(user.password)
    user_id = str(uuid.uuid4())
    new_user = UserInDB(username=user.username, hashed_password=hashed_password, user_id=user_id)
    fake_users_db[user.username] = new_user
    return new_user

# Authenticate a user by username and password
async def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    """
    Authenticate a user by username and password.
    """
    user = fake_users_db.get(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# Generate an access token for the user
def generate_token(user: UserInDB):
    """
    Generate an access token for the user.
    """
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return access_token
