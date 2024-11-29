import logging
from fastapi import FastAPI, APIRouter, HTTPException, Depends, Request
from app.models.user import UserCreate, Token
from app.services.user_service import create_user, authenticate_user, generate_token
from fastapi.security import OAuth2PasswordRequestForm

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

router = APIRouter()

@router.post("/register", status_code=201, summary="Register a new user", tags=["users"])
async def register_user(user: UserCreate):
    """
    Register a new user by providing a username and password.
    Returns the username if registration is successful.
    """
    try:
        created_user = await create_user(user)
        return {"username": created_user.username, "user_id": created_user.user_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login", response_model=Token, summary="User login", tags=["users"])
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticate a user and generate an access token for API usage.
    Requires a username and password.
    """
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = generate_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
