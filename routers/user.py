from fastapi import APIRouter, Depends, Response, status
import schema, database
from sqlalchemy.orm import Session
from repository import user

router = APIRouter(
    prefix="/user",
    tags=["User"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ShowUser)

def create_user(request: schema.User, db: Session = Depends(database.get_db)):
    return user.create(request, db)


@router.get("/{id}",status_code=status.HTTP_200_OK, response_model= schema.ShowUser)

def show_user(id: int,  response: Response ,db: Session = Depends(database.get_db)):
    return user.show(id, response)
    