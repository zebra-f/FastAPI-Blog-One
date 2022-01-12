from fastapi import FastAPI, Depends, status, Response, HTTPException
import fastapi
from pydantic import BaseModel
from sqlalchemy.orm import Session

from . import schemas, models
from .database import engine, SessionLocal


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {
        '/docs': 'Swahher UI documentation',
        '/redoc': 'ReDoc documentation'
        }


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create(blog: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blog')
def get_blogs(db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=200)
def get_blog(id: int, response: Response, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f"id {id} is not aviable."}