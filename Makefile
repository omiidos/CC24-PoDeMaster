# Makefile

# Install dependencies
install:
	pip install -r requirements.txt

# Run tests with pytest
test:
	pytest

# Run the FastAPI application
run:
	uvicorn main:app --reload
