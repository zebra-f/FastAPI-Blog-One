from pydantic import BaseModel
from typing import List, Optional

# USER ---- USER ---- USER --------
# USER ---- USER ---- USER ------
# USER ---- USER ---- USER ----

class User(BaseModel):
    name: str
    email: str
    password: str


class UserNameEmail(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True

# BLOG ---- BLOG ---- BLOG --------
# BLOG ---- BLOG ---- BLOG ------ 
# BLOG ---- BLOG ---- BLOG ---- 

class Blog(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True   


class BlogTitleBodyAuthor(BaseModel):
    title:str
    body: str
    author: UserNameEmail

    class Config:
        orm_mode = True


class BlogTitle(BaseModel):
    title: str
    
    class Config:
        orm_mode = True

# USER ---- USER ---- USER --------
# USER ---- USER ---- USER ------
# USER ---- USER ---- USER ----

class UserNameEmailBlogs(BaseModel):
    name: str
    email: str
    blogs: List[Blog]


    class Config:
        orm_mode = True

# LOGIN ---- LOGIN ---- LOGIN --------
# LOGIN ---- LOGIN ---- LOGIN ------
# LOGIN ---- LOGIN ---- LOGIN ----

class Login(BaseModel):
    email: str
    password: str

# TOKEN ---- TOKEN ---- TOKEN --------
# TOKEN ---- TOKEN ---- TOKEN ------
# TOKEN ---- TOKEN ---- TOKEN ----

# class Token(BaseModel):
#     access_token: str
#     token_type: str


# class TokenData(BaseModel):
#     email: Optional[str] = None