from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
from models import Base, Todo
from schemas import TodoCreate, TodoUpdate, TodoResponse



Base.metadata.create_all(bind=engine)


app = FastAPI(title="Todo API")



# CREATE A TODO

@app.post(
    "/todos", 
    response_model=TodoResponse,
    status_code= status.HTTP_201_CREATED,
)

def create_todo(payload:TodoCreate, db: Session = Depends(get_db)):
    todo = Todo(**payload.model_dump())
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo
