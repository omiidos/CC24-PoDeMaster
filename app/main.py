# app/main.py
import logging
from fastapi import FastAPI, Request
from app.routes import pokemon, user

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app instance
app = FastAPI()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response: {response.status_code}")
    return response

# Default route
@app.get("/")
async def root():
    return {"message": "Welcome to the Pokémon API!",
            "details": "This API allows you to manage Pokémon and users. Navigate to /docs for the Swagger UI or /redoc for the ReDoc UI."
    }
            

# Include Pokémon and User routes
app.include_router(pokemon.router, prefix="/pokemons", tags=["pokemon"])
app.include_router(user.router, prefix="/users", tags=["users"])