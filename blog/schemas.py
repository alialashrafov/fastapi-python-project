from typing import List, Optional
from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str




class User(BaseModel):
    name: str
    email: str
    password: str
        
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]
    
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    
class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None