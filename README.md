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