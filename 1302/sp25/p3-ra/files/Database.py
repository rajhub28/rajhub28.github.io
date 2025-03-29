from Relation import *
from Tuple import *

class Database:

	def __init__(self):
		self.relations = {}

	# Add relation r to Dictionary if relation does not already exists.
	# return True on successful add; False otherwise
	def addRelation(self,r):
		pass

	# Delete relation r from Dictionary if relation exists. 
	# return True on successful delete; False otherwise
	def deleteRelation(self,rname):
		pass

	# Retrieve and return relation with name rname from Dictionary.
	# return None if it does not exist.
	def getRelation(self, rname):
		pass

	# Return database schema as a String
	# Please see sample runs for how schema should be formatted
	def displaySchema(self):
		pass

	# Return entire database as a String
	# Basically concatenate str(r) for each r in the database
	def __str__(self):
		pass

	# reads data from files stored within "dir" and constructs the
	# Database, Relation, and Tuple objects and connects them.
	# You can assume that the files in "dir" conains catalog.dat and
	# related files and are all valid.
	def initializeDatabase(self, dir):
		pass

