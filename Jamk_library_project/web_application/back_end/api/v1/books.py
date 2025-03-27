from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookResponse
from app.core.security import get_current_user, get_current_admin

router = APIRouter()

@router.post("/", response_model=BookResponse, dependencies=[Depends(get_current_admin)])
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.get("/", response_model=list[BookResponse], dependencies=[Depends(get_current_user)])
def list_books(db: Session = Depends(get_db)):
    return db.query(Book).all()
