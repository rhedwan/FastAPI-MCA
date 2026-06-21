from fastapi import FastAPI, Response, status
from pydantic import BaseModel, Field, EmailStr
app = FastAPI()


@app.get("/")
def home():
    age =  2026 - 1995
    sum = 0 
    for i in range(1, 100):
        sum += i
    return {"message": "Welcome to the FastAPI application!", 
            "age": age, 
            "sum": sum}


@app.get("/student")
def student():

    names = ["Sakeenah", "Aishat", "Naheemot", "Aminat"]
    return {
        "student": names
    }


@app.get("/student/{student_id}")
def student(student_id: int):

    names = ["Sakeenah", "Aishat", "Naheemot", "Aminat", "Rodiat"]
    try: 
        student_name = names[student_id]
        return {
            "student_name": student_name,
            "serial_number": student_id
        }
    except:
        return Response("User not found", status_code=404)



@app.get("/teacher")
def student(level:str = "beginner"):

    return {
        "level": f"You are a {level}"
    }


@app.get("/post")
def posts(limit:int, page:int=1):

    # 


    return {
        "page": page,
        "limit": limit
    }

class Student(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=8,
        default="Ridwan"
    )
    email:  EmailStr
    year_of_birth: int = Field(
        ge=2006,
        le=2026,
    )
    is_active: bool 


@app.post("/student", status_code=status.HTTP_201_CREATED)
def create_student(student: Student):
   
    return {
        "message": "Student created",
        "student": student
    }