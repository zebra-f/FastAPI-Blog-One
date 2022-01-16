from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from .. import schemas, models
from ..database import get_db
from ..pwd import verify_password


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)


@router.post("/")
def login(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if user and verify_password(request.password, user.password):
        return 'Hello'
    else: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Wrong credentials")