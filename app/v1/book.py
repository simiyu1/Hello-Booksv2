books_list = [] #Database with all book information

class Book(object):
    """A book in the library or borrowed

	Attributes:
        ISBN: An integer holding a unique book number.
        title: A string holding the book title.
        author: A string holding the writer name.
        edition: An integer holding the version number.
        publisher: A string holding the publishing house.
        copies: An integer holding the number of copies of the book.
	"""
    def default(self, args):
        invalid_command = args.split(' ')[0]
        print(invalid_command, 'Command Does Not exist')
        
    def __init__(self ):
        self.ISBN = 0
        self.title = 'none'
        self.author = 'none'
        self.edition = 0
        self.publisher = 'none'
        self.copies = 0
        
    def do_add_book(self, ISBN, title, author, edition, publisher, copies):
        """book_information(dict): User book_information
        
        Usage:
        add_book <title> <author> <publisher> <copies>
        """
        #TODO
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.edition = edition
        self.publisher = publisher
        self.copies = copies
        pass
        
    def do_borrow_book(self, book_information):
        """book_information(dict): User book_information
        
        Usage:
        borrow_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass
        
    def do_delete_book(self, book_information):
        """book_information(dict): User book_information
        
        Usage:
        delete_book <title> <author> <publisher> <copies>
        """
        #TODO books_list.delete_book(self, book_information)
        pass
        
    def do_update_book(self, book_information):
        """book_information(dict): User book_information
        
        Usage:
        update_book <title> <author> <publisher> <copies>
        """
        #TODO  books_list.update_book(self, book_information)
        pass

    @staticmethod
    def get_book_by_isbn(ISBN):
        for book in books_list:
            if book.ISBN == book_id:
                return book
        return None

