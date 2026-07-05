from fastapi import FastAPI, Response, status, HTTPException, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
from schemas import AuthorResponse, AuthorCreate, BookCreate, BookResponse
from models import Author, Book


app = FastAPI()


@app.get("/")
def home():
    return "I'm am learning about database relationships."



@app.post("/authors", response_model=AuthorResponse, status_code=201)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    new_author = Author(
        name= author.name
    )

    db.add(new_author)
    db.commit()
    db.refresh(new_author)

    return new_author



@app.get("/authors", response_model=list[AuthorResponse])
def get_authors( db: Session = Depends(get_db)):
    authors  = db.query(
        Author
    ).all()

    return authors


@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    author = db.get(Author, book.author_id)


    if author is None:
        raise HTTPException(
            status_code=404, detail="Author not found"
        )
    

    new_book = Book(
        name = book.name,
        published_year=book.published_year,
        author_id=book.author_id
    )


    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book