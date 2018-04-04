class User(object):

	def __init__(self, userid, username, password):
		self.userid = userid
		self.username = username
		self.password = password
		self.borrowed_books = []
		self.returned_books = []
