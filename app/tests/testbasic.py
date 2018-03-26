import unittest
from v1.book import Book

# test here
"""
Book(dict)
normal: {title->string, author->string, edition->string, copies->number}
boundaries: {title -> "", "   ", 0777: author -> "", "   ", 0777: 
    edition -> "", "   ", 0777: copies -> [0, string, empty, -1, ]}
edge: {author -> "too long ", }
unexpected: {dict, list, file, }
"""

class AddBookTestCase(unittest.TestCase):
    def test_title_is_not_empty_string(self):
        pass

    def test_title_is_not_string(self):
        pass

    def test_copies_is_not_int(self):
        pass

    def test_unexpected_input(self):
        pass


if __name__ == '__main__':
    unittest.main()