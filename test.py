# YouTube video used for this learning exercise is :
            # https://www.youtube.com/watch?v=7t2alSnE2-I&t=1038s

# ----------------------------------------------- Imports -----------------------------------------------
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# ---------------------------------------- Create Instance -----------------------------------------------
app = FastAPI() # Creating Instance of App

# --------------------------------------------- Basic Path -----------------------------------------------
@app.get("/") # Simple / is Base path

def index():
    return {'data': {'name': 'Kumail'}}

#----------------------------------------------- About Path -----------------------------------------------
@app.get("/about") # path after / is defined path

def about():
    return {'data': "About Page"}
    
# -------------------------------------------- Unpublished Path --------------------------------------------
@app.get("/blog/unpublished")
# Put /blog/unpub above the /blog/id: int as Reads line-by-line, will cause type error

def unpublished():
    return {'data': "all Unpublished Blogs"}

# -------------------------------------------- Query for a blogs ---------------------------------------------
@app.get("/blog")

def get_blog(limit: int =10, published: bool= True): # these are Queries set to INT and BOOl
                        # Query is done as: "?" after the "/" , the "&" for space and "=" for value
    
    if published:
       return {'data': f'{limit} published blogs for now.'}
    else:
        return {'data': f'{limit}  blogs for now.'}
    

# -------------------------------------------- Blog id Dynamic ---------------------------------------------
@app.get("/blog/{id}") # given Dynamic Path as variable (will adopt with it)

def get_blog(id: int): #specified type INT which will cause erorr if something else comes|
    return {'data': id}

# ---------------------------------------------- Blog Comments ---------------------------------------------
@app.get("/blog/{id}/comments") # comments is present for all IDs

def get_comments():
    return {'Comments': {"1","2"}}

# ---------------------------------------------- POST Method---------------------------------------------


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None

@app.post("/blog")

def create_blog(request: Blog):
    return {"data": f"Blog created as: Title: {request.title} and Body: {request.body}"}