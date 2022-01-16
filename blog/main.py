from fastapi import FastAPI

from .routers import blog, user, login
from . import schemas, models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog-One"
    )
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.router)


@app.get('/')
def index():
    return {
        "/docs": {
            "Swahher UI documentation default URL": "http://127.0.0.1:8000/docs"},
        "/redoc": {
            "ReDoc documentation default URL": "http://127.0.0.1:8000/redoc"}
        }
