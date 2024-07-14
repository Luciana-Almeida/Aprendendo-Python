from fastapi import FastAPI
from app.routers import atletas
from fastapi_pagination import add_pagination

app = FastAPI()

app.include_router(atletas.router)
add_pagination(app)
