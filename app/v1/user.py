class User(object):
    """A person using the API

	Attributes:
        fName: A string holding the first name.
        sName: A string holding the second name.
        idNo: An integer holding .
        username: A string holding the username.
        password: A string holding the password.
		useraccess: A string showing access privileges.
	"""
    __metaclass__ = ABCMeta
	useraccess = "none"

	def __init__(self, fName, sName, username, idNo, password):
		self.fName = fName
        self.sName = sName
		self.idNo = idNo
        self.username = username
		self.password = password

	def signIn(self, username, password):
		"""
		signing into the API
		"""
		if username == self.username and password == self.password:
			return True
		else:
			return False

    def signOut(self, username, password):
		"""
		signing out of the API
		"""
		if username == self.username and password == self.password:
			return True
		else:
			return False

	def get_book(self):
		"""
		function to get all the books created
		"""

		
class client(User):
    """A client account type."""

    useraccess = "client"

    def user_type(self):
        """"Return a string representing the type of account this is."""
        return 'client'

	def borrow_book(self, book):
		"""
		admin function to borrow books
		"""
		self.books.append(book)

	def return_book(self, book):
		"""
		admin function to return books
		"""


class admin(User):
    """An administrator account type."""

    useraccess = "admin"

    def user_type(self):
        """"Return a string representing the type of account this is."""
        return 'admin'

	def add_book(self, book):
		"""
		admin function to add books
		"""
		self.books.append(book)

	def delete_book(self, book):
		"""
		admin function to delete books
		"""
		self.books.remove(book)