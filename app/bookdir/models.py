class Book(object):
    """A book in the library or borrowed

	Attributes:
        ISBN: An integer holding a unique book number.
        title: A string holding the book title.
        author: A string holding the writer name.
        edition: A string holding the version number.
        publisher: A string holding the publishing house.
        copies: An integer holding the number of copies of the book.
	"""
        
    def __init__(self, ISBN, title, author, edition, publisher, copies):
        """book_information(dict): User book_information
        
        Usage:
        add_book <title> <author> <edition> <publisher> <copies>
        """
        #newISBN = len(books_list) + 1
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.edition = edition
        self.publisher = publisher
        self.copies = copies
        
    