from pydantic import BaseModel

class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: int

    class Config:
        orm_mode = True
