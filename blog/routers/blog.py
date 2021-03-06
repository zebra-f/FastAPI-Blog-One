from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"]
)


                                                        # CREATE ---- CREATE ---- CREATE ---- CREATE
@router.post('/', status_code = status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title = request.title, 
                            body = request.body,
                            author_id = 2)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


                                                        # DELETE ---- DELETE ---- DELETE ---- DELETE
@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first():
        blog.delete(synchronize_session=False)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


                                                        # UPDATE ---- UPDATE ---- UPDATE ---- UPDATE
@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if blog.first():
        blog.update(request.dict())
        db.commit()
        return request
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


                                                        # READ ---- READ ---- READ ---- READ
@router.get('/')
def get_blogs(db: Session = Depends(get_db), 
            current_user: schemas.User = Depends(oauth2.get_current_user)):
    # list of objects e.g. [<blog.models.Blog object at 0x7f68fa1602e0>, 
    #                       <blog.models.Blog object at 0x7f68fa160280>, 
    #                       <blog.models.Blog object at 0x7f68fa160340>]
    # blogs[0].title ---> 'title 1'
    # blogs[1].body ---> 'body 2'
    # blog[2].id ---> 3
    blogs = db.query(models.Blog).all()
    return blogs


@router.get('/titles', 
        response_model = List[schemas.BlogTitle])
def get_blogs_title(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.get('/{id}', status_code = status.HTTP_200_OK, 
        response_model=schemas.BlogTitleBodyAuthor)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()

    if blog:
        return blog
    else:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'details': f"id {id} is not aviable."}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")

# WHATS GOING ON?
@router.get('/test')
def blog_test(current_user: schemas.User = Depends(oauth2.get_current_user)):
    return {"message": "Hello User"}


@router.get('/test2')
def blog_test_2():
    return {"message": "Hello World"}


@router.get('/{id}/title', status_code = status.HTTP_200_OK, 
        response_model=schemas.BlogTitle)
def get_blog_title(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if blog:
        return blog
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")

# TEST TEST TEST

