from sqlalchemy.orm import Session
import models
from hashing import Hash
from fastapi import Depends, HTTPException, status

def create(request, db: Session):
    new_user = models.User(name=request.name, password=Hash.bcrypt(request.password), email=request.email)
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def show(db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"User with id {id} Not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return (f"Id {id} Blog Not Found")
    else:
        return user 

