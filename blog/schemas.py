from pydantic import BaseModel

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

