# FastAPI: USER-PRODUCT

## Required Environment Variables
- DATABASE=postgresql://postgres:postgres@localhost:5432/mydatabase
- SECRET_KEY=mysecretkey

## Install dependencies
pip install -r requirements/base.txt

## Run project
uvicorn app.main:app --reload

## API Docs
http://localhost:8000/docs

## Install Linters dependencies
pip install -r requirements/linters.txt

## Apply Linters
- black app/
- isort app/
- flake8 app/

## TODO:
- Tests coverage with pytest
- Send email notification when admin updates a product (using AWS Lambda => Email provider)
- Record log when a product is consulted (using AWS Lambda => Save log)
- Containerize the app and CI/CD