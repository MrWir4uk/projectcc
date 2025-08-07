from pydantic import BaseModel

class AuthorBase(BaseModel):
    id: int
    name: str
    bio: str 

    class Config:
        from_attributes = True

class BookBase(BaseModel):
    id: int
    title: str
    pages: int
    author: AuthorBase

    class Config:
        from_attributes = True
        

