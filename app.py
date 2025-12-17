# app.py

import streamlit as st
from book import Book, Library

st.set_page_config(page_title="Digital Library System", layout="centered")

st.title("Digital Library System")

# Keep library persistent
if "library" not in st.session_state:
    st.session_state.library = Library()

library = st.session_state.library

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Add Book",
        "Search by Title",
        "Search by Author",
        "Borrow Book",
        "Return Book",
        "View All Books"
    ]
)

# ---------------- ADD BOOK ----------------
if menu == "Add Book":
    st.header("Add New Book")

    title = st.text_input("Title")
    author = st.text_input("Author")
    book_id = st.text_input("Book ID")
    copies = st.number_input("Total Copies", min_value=1, step=1)

    if st.button("Add Book"):
        if book_id in library.books:
            st.error("Book ID already exists.")
        else:
            library.add_book(Book(title, author, book_id, copies))
            st.success("Book added successfully.")

# ---------------- SEARCH TITLE ----------------
elif menu == "Search by Title":
    st.header("Search by Title")
    title = st.text_input("Enter title")

    if st.button("Search"):
        results = library.search_by_title(title)
        if results:
            for book in results:
                st.write(
                    f"**{book.title}** | {book.author} | "
                    f"{book.available_copies}/{book.total_copies} available"
                )
        else:
            st.warning("No books found.")

# ---------------- SEARCH AUTHOR ----------------
elif menu == "Search by Author":
    st.header("Search by Author")
    author = st.text_input("Enter author")

    if st.button("Search"):
        results = library.search_by_author(author)
        if results:
            for book in results:
                st.write(
                    f"**{book.title}** | {book.author} | "
                    f"{book.available_copies}/{book.total_copies} available"
                )
        else:
            st.warning("No books found.")

# ---------------- BORROW BOOK ----------------
elif menu == "Borrow Book":
    st.header("Borrow Book")

    book_id = st.text_input("Book ID")
    user_name = st.text_input("Your Name")

    if st.button("Borrow"):
        message = library.borrow_book(book_id, user_name)
        if "successfully" in message:
            st.success(message)
        else:
            st.error(message)

# ---------------- RETURN BOOK ----------------
elif menu == "Return Book":
    st.header("Return Book")

    book_id = st.text_input("Book ID")
    user_name = st.text_input("Your Name")

    if st.button("Return"):
        message = library.return_book(book_id, user_name)
        if "successfully" in message:
            st.success(message)
        else:
            st.error(message)

# ---------------- VIEW BOOKS ----------------
elif menu == "View All Books":
    st.header("Library Books")

    if not library.books:
        st.info("No books available.")
    else:
        for book in library.books.values():
            st.write(
                f"**ID:** {book.book_id} | "
                f"**Title:** {book.title} | "
                f"**Author:** {book.author} | "
                f"**Available:** {book.available_copies}/{book.total_copies}"
            )
