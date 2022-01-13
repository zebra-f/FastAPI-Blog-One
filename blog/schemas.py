from pydantic import BaseModel


class Blog(BaseModel):
    title: str
    body: str


class GetBlogTitle(BaseModel):
    title: str
    
    class Config:
        orm_mode = True