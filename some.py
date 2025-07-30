from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'Ali Alashrafov'}}

@app.get('/blog')
def index(limit : int = 20, published : bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from database'}
    else:
        return {'data': f'{limit} blogs from the db'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished posts'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data': id}



@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': [{'blogid': id}, '1', '2']}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

@app.post('/blog')
def create_blog(blog: Blog):
    return {'data': f'Blog is created with title as {blog.title}'}