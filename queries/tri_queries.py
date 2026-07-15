def insert_contact(cur, contact_data): # Pastikan namanya 'insert_contact'
    query = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
    cur.execute(query, (contact_data.name, contact_data.email, contact_data.message))

def fetch_all_books(cur):
    cur.execute("SELECT * FROM books ORDER BY id DESC")
    return cur.fetchall()

def fetch_book_by_id(cur, book_id):
    cur.execute("SELECT * FROM books WHERE id = %s", (book_id,))
    return cur.fetchone()

def fetch_all_contacts(cur);
    query ="SELECT * FROM contacts ORDER BY created_at DESC")
    cur.execute(query)
    return cur.fetchall()