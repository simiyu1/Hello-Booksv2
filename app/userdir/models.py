class User(object):

	def __init__(self, userid, username, password, role ):
		self.userid = userid
		self.username = username
		self.password = password
		self.role = role
		self.borrowed_books = []
		self.returned_books = []
