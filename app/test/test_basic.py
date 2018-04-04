import unittest

class AddBookTestCase(unittest.TestCase):
    def test_title_is_not_empty_string(self):
        #app = Book()
        #result = app.do_add_book(475,'', 'Nelly White',5,'Pearson', 112)
        #self.assertEqual(result, "Error book title can not be empty")
        pass

    def test_title_is_not_string(self):
        #app = Book()
        #result = app.do_add_book(475, 3, 'Nelly White',1, 'Pearson', 112)
        #self.assertEqual(result, "Error book title must be a string")
        pass

    def test_copies_is_not_int(self):
        #app = Book()
        #result = app.do_add_book(475, 'The Goblet', 'Nelly White',7,'Pearson', 'three')
        #self.assertEqual(result, "Error copies must be an int.")
        pass

    def test_unexpected_input(self):
        #app = Book()
        #result = app.do_add_book([],3, 'Nelly White',1, 'Pearson', 112 )
        #self.assertEqual(result, "Error unexpected input.")
        pass

if __name__ == '__main__':
    unittest.main()