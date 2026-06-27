from datetime import datetime
from pydantic import BaseModel, ConfigDict



class TodoBase(BaseModel): 
    title: str
    description: str | None = None
    completed: bool = False


#For POST - what we expect the client (browser) to send
class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None


class TodoResponse(TodoBase): 
    id: int

    created_at = datetime
    model_config = ConfigDict(from_attributes=True)




# class TodoResponse(BaseModel): 
#     id: int


#     title: str
#     description: str | None = None
#     completed: bool = False

#     created_at = datetime
#     model_config = ConfigDict(from_attributes=True)

