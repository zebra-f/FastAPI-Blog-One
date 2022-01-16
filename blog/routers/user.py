from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db
from ..pwd import get_password_hash, verify_password


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


                                                        # CREATE ---- CREATE ---- CREATE ---- CREATE
@router.post('/', status_code = status.HTTP_201_CREATED, 
        response_model = schemas.UserNameEmail)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name = request.name, 
                            email = request.email, 
                            password = get_password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


                                                        # READ ---- READ ---- READ ---- READ
@router.get('/', status_code = status.HTTP_200_OK,
        response_model = List[schemas.UserNameEmail])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.get('/{id}', status_code = status.HTTP_200_OK, 
        response_model = schemas.UserNameEmail)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    # print(user.blogs[0].title)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")


@router.get('/{id}/blogs', status_code = status.HTTP_200_OK, 
        response_model = schemas.UserNameEmailBlogs)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    # print(user.blogs[0].title)
    if user:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"id {id} is not aviable.")