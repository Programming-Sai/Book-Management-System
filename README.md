# Book Management System

This is a Python-based command-line application for managing a collection of books. Users can add, remove, update, search, and view details of books stored in a text file (`Books.txt`).

## Setup

### Clone the repository
   ```bash
   git clone https://github.com/Programming-Sai/Book-Management-System.git
   cd Book-Management-System
   ```
2. Install dependencies:

```bash
# Ensure you have Python installed (version 3.x recommended)
pip install tabulate
```

### Create a Books.txt file

- Create a file named Books.txt where the book data will be stored. Each line in Books.txt should follow the format: title,author,genre,description.


### Usage
Run the program by executing `Book_Management_System.py`:

```bash

python Book_Management_System.py
```

### Command-Line Interface (CLI) Options
1. View Books: Displays a list of all books.
2. Add Book: Adds a new book to the collection.
3. Remove Book: Deletes a selected book from the collection.
4. Search For Book: Finds books based on title, author, genre, or description.
5. Update Book Details: Modifies information about a specific book.
6. Show Book Details: Displays detailed information about a selected book.
7. Clear Book List: Deletes all books from the collection.


### File Structure


main.py: Main script to run the Book Management System.
Books.txt: Text file storing book data.
README.md: This file providing an overview and instructions.

```graphql
./Book-Management-System/*
    ├─ Book_Management_System.py # main file hodling all book operations.
    ├─ Books.txt # Holds all books added
    └─ README.md
```
