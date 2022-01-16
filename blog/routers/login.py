from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from datetime import timedelta

from .. import schemas, models
from ..database import get_db
from ..pwd import verify_password
from ..jwt import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post("/", status_code=status.HTTP_202_ACCEPTED)
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    
    if user and verify_password(request.password, user.password):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}
    
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Wrong credentials")