from sqlalchemy.orm import Session
import models
from fastapi import APIRouter, Depends, HTTPException, Response, status

def create(db, request):
    new_blog = models.Blog(title=request.title, body=request.body, user_id = request.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def delete(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with id {id} not found")
    else:
        db.delete(blog)
        db.commit()
    return {"detail": "Deleted"}

def update(new_body, new_title, db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog with id {id} not found")
    else:
        blog.title = new_title
        blog.body = new_body
        db.commit()
        return {"detail": f"""Updated... New title: "{new_title}", New Body: "{new_body}"..."""}
    
def  show(db: Session, id):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Id {id} Blog Not Found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return (f"Id {id} Blog Not Found")
    else:
        return blog 
    
def show_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs