from typing import Optional
from fastapi import FastAPI


app  = FastAPI()

@app.get('/blog')
def index(limit: int=10, published: bool=True, sort: Optional[str]=None):
    
    if published:
        return {
            "data": f"{limit} PUBLISHED blogs from blog db list" 
            }
    else:
        return {
            "data": f"{limit} NOT PUBLISHED blogs from blog db list, {sort}" 
            }


@app.get('/blog/unpublished')
def unpublished():
    return {
        "data": "all unpublished blogs"
        }



@app.get('/blog/{id}')
def show(id: int):
    return {
        "data": id
    }


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    return limit
    return {
        "data": ["1", "2"]
    }


@app.post('/blog')
def create_blog():
    return {"data": "Blog is created"}