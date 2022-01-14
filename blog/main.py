from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import schemas, models
from .database import engine, SessionLocal
from .pwd import get_password_hash, verify_password


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Blog-One"
    )

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ENDPOINTS ---- ENDPOINTS ---- ENDPOINTS --------
# ENDPOINTS ---- ENDPOINTS ---- ENDPOINTS ------
# ENDPOINTS ---- ENDPOINTS ---- ENDPOINTS ----


@app.get('/')
def index():
    return {
        '/docs': 'Swahher UI documentation',
        '/redoc': 'ReDoc documentation'
        }

# BLOGS ---- BLOGS ---- BLOGS --------
# BLOGS ---- BLOGS ---- BLOGS ------
# BLOGS ---- BLOGS ---- BLOGS ----    

                                                        # CREATE ---- CREATE ---- CREATE ---- CREATE
@app.post('/blogs', status_code=status.HTTP_201_CREATED,
        tags=["Blogs"])
def create_blog(request: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title = request.title, 
                            body = request.body,
                            author_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


                                                        # DELETE ---- DELETE ---- DELETE ---- DELETE
@app.delete('/blogs/{id}', status_code=status.HTTP_204_NO_CONTENT, 
        tags=["Blogs"])
def delete_blog(id: int, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first():
        blog.delete(synchronize_session=False)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


                                                        # UPDATE ---- UPDATE ---- UPDATE ---- UPDATE
@app.put('/blogs/{id}', status_code=status.HTTP_202_ACCEPTED,
        tags=["Blogs"])
def update_blog(id: int, request: schemas.Blog, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first():
        blog.update(request.dict())
        db.commit()
        return request
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


                                                        # READ ---- READ ---- READ ---- READ
@app.get('/blogs',
        tags=["Blogs"])
def get_blogs(db: Session=Depends(get_db)):
    # list of objects e.g. [<blog.models.Blog object at 0x7f68fa1602e0>, 
    #                       <blog.models.Blog object at 0x7f68fa160280>, 
    #                       <blog.models.Blog object at 0x7f68fa160340>]
    # blogs[0].title ---> 'title 1'
    # blogs[1].body ---> 'body 2'
    # blog[2].id ---> 3
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blogs/titles', response_model=List[schemas.BlogTitle],
        tags=["Blogs"])
def get_blogs_title(db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blogs/{id}', status_code=status.HTTP_200_OK, response_model=schemas.BlogTitleBodyAuthor,
        tags=["Blogs"])
def get_blog(id: int, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f"id {id} is not aviable."}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


@app.get('/blogs/{id}/title', status_code=status.HTTP_200_OK, response_model=schemas.BlogTitle,
        tags=["Blogs"])
def get_blog_title(id: int, db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")

# USERS ---- USERS ---- USERS --------
# USERS ---- USERS ---- USERS ------
# USERS ---- USERS ---- USERS ----   

                                                        # CREATE ---- CREATE ---- CREATE ---- CREATE
@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=schemas.UserNameEmail,
        tags=["Users"])
def create_user(request: schemas.User, db: Session=Depends(get_db)):
    new_user = models.User(name = request.name, 
                            email = request.email, 
                            password = get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


                                                        # READ ---- READ ---- READ ---- READ
@app.get('/users', status_code=status.HTTP_200_OK, response_model=List[schemas.UserNameEmail],
        tags=["Users"])
def get_users(db: Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users


@app.get('/users/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserNameEmail,
        tags=["Users"])
def get_user(id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    # print(user.blogs[0].title)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


@app.get('/users/{id}/blogs', status_code=status.HTTP_200_OK, response_model=schemas.UserNameEmailBlogs,
        tags=["Users"])
def get_user(id: int, db: Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    # print(user.blogs[0].title)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")