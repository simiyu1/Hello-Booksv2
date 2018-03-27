# Hello-Booksv2
This is a python based API that keeps library transaction records.

Specifications

| EndPoint | EndPoint |
| ------------- | ------------- |
| PUT /api/books/<bookId> |modify a book’s information  |
|DELETE /api//books/<bookId> | Remove a book  |
| GET /api/books | Retrieves all books |
| GET /api/books/<bookId> | Get a book |
| POST /api/users/books/<bookId> | Borrow a book  |
| POST /api/auth/register | Creates a user account |
| POST /api/auth/login | Logs in a user |
| POST /api/auth/logout | Logs out a user |
| POST /api/auth/reset-password | Password reset |
|  |  | 
  
*Installation*
   i. Clone or download the repository
      `git clone https://github.com/simiyu1/Hello-Booksv2/develop/`
   ii. Create a virtual environment
      `virtualenv venv`
      In windows `mkvirtualenv venv`
   iii. Activate the environment 
      `source venv\bin\activate`
      in windows use `venv/Scripts/activate`
   iv. Install the environmmental requirements from the file within the virtual venv
       `pip install -r requirements.txt`
   v. Running the tests
        `python -m unittest discover -v` (Runs all tests in windows)

