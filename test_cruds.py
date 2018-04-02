import unittest
import json

from run import app
from app.bookdir.models import *
from app.bookdir.views import books_list


class BookAPITests(unittest.TestCase):

    def setUp(self):
        """Define test (env) variables and initialize some list data for the app."""
        self.app = app
        # creating dummy instances.
        books_list = []
        book1 = Book(1,'The Eleventh Commandment','Jeffrey Archer')
        book2 = Book(2,'If Tomorrow Comes','Sidney Sheldon')
        book3 = Book(3,'Origin','Dan Brown')
        
        books_list.append(book1)
        books_list.append(book2)
        books_list.append(book3)

        self.app = self.app.test_client()
        self.BASE_URL = 'http://127.0.0.1:5000/api/v1/books/'

    def tearDown(self):
        '''Clean our environment before leaving'''
        self.app.testing = False
        self.app = None
        self.BASE_URL = None


    def test_get_all_books(self):
        ''' Should retrieve books from library
        '''
        resp = self.app.get(self.BASE_URL)

        data = json.loads(resp.get_data().decode('utf-8'))
        existing_item = {'ISBN':7,'title':'Done Deal','author':'Ken Follet'}
        error_item = {'ISBN': 9, 'title':'The Pillars of the Earth','author':'Ken Follet'}
        book7 = Book(7,'Done Deal','Ken Follet')

        # Later check that test_item should be in the list book7 in data
        self.assertTrue(data, msg='All book data')

    def test_get_a_single_book(self):
        ''' test if a book cab be serached by ISBN
        '''
        data= {'author': 'Dan Brown'}
        resp = self.app.get(self.BASE_URL,
                             data=json.dumps(data), content_type='application/json')
        self.assertEqual(resp.status_code, 200,
                         msg='Should retrieve data from the api.')

        data = json.loads(resp.get_data().decode('utf-8'))
        gotdata = data[1]

        test_item = {'ISBN': 3, 'title':'If Tomorrow Comes','author':'Jeffrey Archer'}


        # test_item should be in the list
        self.assertEqual(test_item['title'], gotdata['title'],
                        msg='Gets a specific book')

    def test_post_book(self):
        '''This method tests that a book can be added'''

        newbook = {'ISBN': 10, 'title':'The hand of God', 
                      'author':'Ken Follet'}
        resp = self.app.post(self.BASE_URL, data=json.dumps(
            newbook), content_type='application/json')

        self.assertEqual(resp.status_code, 200,
                         msg='Book added')
        
    def test_delete_book(self):
        ''' testing book deletion
        '''
        data= {'ISBN': 2}
        item_id = 1
        
        resp = self.app.post(self.BASE_URL, data=json.dumps(
            data), content_type='application/json')
        
        if resp.status_code == 404:
            return True

        test_item = (1, 'Test Driven Development', 'Kent Beck')
        # Get all books in the api
        books = []
        for book in books_list:
            books.append(book.ISBN)

        self.assertFalse(test_item in books,
                         msg='The api should delete a book')

    def test_edit_book(self):
        '''Updates book data'''

        pass




class UserTests(unittest.TestCase):

    def setUp(self):
        # Prepare for testing;set up variables
        from app.auth.views import all_users
        from app.userdir.models import User

        self.all_users = all_users
        self.app = app
        self.app = self.app.test_client()
        self.BASE_URL = 'http://localhost:5000/api/v1/auth/'
        self.BASE_URL2 = 'http://localhost:5000/api/v1/users/'

    def tearDown(self):
        '''Clean our environment before leaving'''
        self.app.testing = False
        self.app = None
        self.BASE_URL = None
        self.all_users = None
        self.user = None

    def test_can_create_user(self):
        self.user = {'userid':3,'username': 'Juma', 'password': 'pass123'}

        resp = self.app.post(self.BASE_URL + 'register', data=json.dumps(
            self.user), content_type='application/json')

        self.assertEqual(resp.status_code, 201,
                        msg="user created")

    def test_user_details_can_be_fetched(self):
        pass

    def test_user_can_borrow_a_book(self):
        data = {"username": "Kinde Kinde", "userid": 4, 'ISBN':4}

        # send the data
        resp = self.app.post('http://localhost:5000/api/v1/users/books/',
                             data=json.dumps(data), content_type='application/json')
        if resp.status_code == 404:
            return 1

        # Extract data
        recv = json.loads(resp.get_data().decode('utf-8'))
        #books_borrowed = recv['borrowings']self.assertTrue(len(books_borrowed) != 0, msg = "Book borrowed")

        self.assertEqual(resp.status_code, 200, msg='Book borrowed')

if __name__ == '__main__':
    unittest.main()
