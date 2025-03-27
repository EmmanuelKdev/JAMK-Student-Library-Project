# School Library System Architecture

## 1. Overview
The school library system will enable:
- Book Management (CRUD for books)
- Student Management (CRUD for students) 
- Borrow & Return Books
- Authentication & Authorization (Admin & Students)
- Database Integration (SQLAlchemy with PostgreSQL or SQLite)

## 2. File Structure Breakdown

### `app/main.py`
- Entry point for the FastAPI app
- Includes app initialization and API routers

### `app/core/`
- `config.py`: Stores application settings
- `security.py`: Handles authentication (JWT, OAuth2)

### `app/db/`
- `session.py`: Handles database session
- `base.py`: Defines base models for ORM

### `app/models/`
Defines SQLAlchemy ORM models for:
- Book
- Student  
- BorrowedBook

### `app/schemas/`
- Pydantic models for data validation

### `app/services/`
- Contains business logic (e.g., borrowing logic)

### `app/api/v1/endpoints/`
Houses API route handlers for:
- `books.py` (CRUD operations for books)
- `students.py` (CRUD for students)
- `borrow.py` (Borrowing system)

### `app/tests/`
- Unit and integration tests for API endpoints