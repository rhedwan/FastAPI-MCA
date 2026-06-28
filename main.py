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


#READ (all)
@app.get("/todos", response_model=list[TodoResponse])
def list_todos(
    completed:bool | None = None, 
    search: str | None = None,
    db: Session = Depends(get_db)):
    query =  db.query(Todo)

    if completed is not None:
        query = query.filter(Todo.completed == completed)


    if search: 
        query = query.filter(Todo.title.ilike(f"%{search}%"))

        

    return query.all()



#  READ (one)
@app.get('/todos/{todo_id}', response_model=TodoResponse)
def get_todo(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    
    return todo


# UPDATE
@app.put('/todos/{todo_id}', response_model=TodoResponse)
def update_todo(todo_id:int, payload: TodoUpdate, db: Session = Depends(get_db)):

    todo = db.query(Todo).filter(Todo.id == todo_id).first() 

    # None or False

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")
    


    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)

    
    db.commit()
    db.refresh(todo)
    return todo



# DELETE 
@app.delete('/todos/{todo_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id:int, db: Session = Depends(get_db)):

    todo = db.query(Todo).filter(Todo.id == todo_id).first() 

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found!")

    db.delete(todo)
    db.commit()



    # C -> Create R-> Read U-Update D-Delete