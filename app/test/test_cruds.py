import unittest
import os
import json
from v1 import create_app

class booksTestCase(unittest.TestCase):
    """In this class we shall be testing the API endpoints"""

    def setUp(self):
        """Define test variables and initialize some list data for the app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.book = {'ISBN': '475', 'title':'Night train to Istanbull','author':'Penny Mice',
                      'edition':'1','publisher':'Pearson','copies':'54'}


    def test_book_creation(self):
        """Test API can create a book add request (POST request)"""
        res = self.client().post('/api/books/', data=self.book)
        self.assertEqual(res.status_code, 201)
        self.assertIn(book, str(res.data))

    def test_api_can_get_all_book(self):
        """Test API can get all entries (GET request)."""
        res = self.client().post('/api/books/', data=self.book)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/api/books/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(book, str(res.data))

    def test_api_can_get_book_by_id(self):
        """Test API can get a single book entry by using it's isdn."""
        rv = self.client().post('/api/books/', data=self.book)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/booklists/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn(book, str(result.data))

    def test_book_can_be_edited(self):
        """Test API can edit an existing book entry. (PUT request)"""
        rv = self.client().post(
            '/api/books/',
            data={'isbn': 1, 'title':'The Mirage', 'author':'nicole kidman',
                    'edition':3,'publisher':'Pearson', 'copies':4})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/api/books/',
            data={
                "name": "Dont just eat, but also pray and love :-)"
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/api/books/')
        self.assertIn('Dont just eat', str(results.data))

    def test_book_deletion(self):
        """Test API can delete a book entry. (DELETE request)."""
        rv = self.client().post(
            '/api/books/',
            data={'isbn': 1, 'title':'The Mirage', 'author':'nicole kidman',
                    'edition':3,'publisher':'Pearson', 'copies':4})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/booklists')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/api/books/')
        self.assertEqual(result.status_code, 404)

    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
