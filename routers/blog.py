from fastapi import APIRouter, Depends, HTTPException, Response, status
import schema, models, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from repository import blog



router = APIRouter(
    prefix="/blog",
    tags=["Blog"]
)

db = database.get_db
@router.post("/", status_code=status.HTTP_201_CREATED,)

def create_blog(request: schema.CreateBlog, db: Session = Depends(database.get_db),
                current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.create(db, request)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)

def delete_blog(id: int, response: Response ,db: Session = Depends(database.get_db),
                current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.delete(db, id)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)

def update_blog(new_title: str, new_body: str, id: int,
                response: Response ,db: Session = Depends(database.get_db),
                current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.update(new_body, new_title, db, id)

@router.get("/", response_model= List[schema.ShowBlog])

def get_all_blogs(db: Session = Depends(database.get_db),
                  current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.show_all(db)

@router.get("/{id}",status_code=status.HTTP_200_OK, response_model= schema.ShowBlog)

def show_blog(id: int,  response: Response ,db: Session = Depends(database.get_db),
              current_user: schema.User = Depends(oauth2.get_current_user)):
    return blog.show(db, id)