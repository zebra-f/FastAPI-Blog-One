from fastapi import FastAPI

from .routers import blog, user
from . import schemas, models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog-One"
    )
app.include_router(blog.router)
app.include_router(user.router)


@app.get('/')
def index():
    return {
        '/docs': 'Swahher UI documentation',
        '/redoc': 'ReDoc documentation'
        }
