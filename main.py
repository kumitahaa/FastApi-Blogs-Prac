from fastapi import FastAPI

app = FastAPI()

todos = []

@app.get("/")

def index():
    return {'data': {'name': 'Kumail'}}


@app.get("/about")

def about():
    return {'data': "About Page"}
