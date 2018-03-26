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

    def argument_parser(fn):
        '''
        input fn -> function
        return -> a fuction that can parse commandline args using docopt.

        This function re-used as-is(without alteration) from the TDD intro class
        '''
        def get_args(self, args):
            try:
                print(type(args))
                opt = docopt(fn.__doc__, args)
                return fn(self, opt)
            except DocoptExit as e:
                print(e, "Malformed Command")
        return get_args

    def default(self, args):
        invalid_command = args.split(' ')[0]
        print(invalid_command, 'Command Does Not exist')


	def __init__(self, ISBN, title, author, edition, publisher, copies):
		self.ISBN = ISBN
        self.title = title
		self.author = author
        self.edition = edition
		self.publisher = publisher
        self.copies = copies

    @argument_parser
    def do_add_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                add_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

    @argument_parser
    def do_borrow_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                borrow_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

    @argument_parser
    def do_delete_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                delete_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

    @argument_parser
    def do_update_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                update_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

	