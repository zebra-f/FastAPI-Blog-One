from pydantic import BaseModel

# BLOG ---- BLOG ---- BLOG --------
# BLOG ---- BLOG ---- BLOG ------ 
# BLOG ---- BLOG ---- BLOG ---- 

class Blog(BaseModel):
    title: str
    body: str


class BlogTitle(BaseModel):
    title: str
    
    class Config:
        orm_mode = True

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

