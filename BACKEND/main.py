from fastapi import FastAPI
from routers import router
from core.config import settings
from database.database import create_tables

create_tables()

app = FastAPI(title=settings.APP_NAME)

app.include_router(router.router)

@app.get("/", tags=['Root'])
def read_root():
    return {"Message": "Welcome to the Personality API. Go to /docs for documentation."}