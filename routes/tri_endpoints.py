from fastapi import APIRouter, HTTPException
from database import get_db_connection
from models.tri_models import ContactIn
from queries.tri_queries import insert_contact, fetch_all_books, fetch_book_by_id, fetch_all_contacts

router = APIRouter()

@router.get("/api/books")
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    books = fetch_all_books(cur)
    cur.close()
    conn.close()
    return books

@router.post("/api/contact")
def post_contact(contact: ContactIn):
    conn = get_db_connection()
    cur = conn.cursor()
    insert_contact(cur, contact)
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Success"}

@router.get("/api/books/{book_id}")
def get_book_detail(book_id: int):
    try:
        conn = get_db_connection()
        cur = conn.cursor()


        book = fetch_book_by_id(cur, book_id)

        cur.close()
        conn.close()

        if book:
            return book
        else:
            raise HTTPException(status_code=404, detail="Book not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/api/contacts")
def get_all_messages():
    try:
        conn = get_db_connection()
        cur =conn.cursor()
        messages = fetch_all_contacts(cur)
        cur.close()
        conn.close()
        return messages
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))