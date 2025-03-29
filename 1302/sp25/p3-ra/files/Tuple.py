class Tuple:

	def __init__(self,attributes):
		self.attributes = attributes
		self.tuple = []

	# Add a tuple component to the end of the tuple
	def addComponent(self, comp):
		pass

	# Return String representation of tuple; See output of run for format.
	def __str__(self):
		pass

	# returns True if self and compareTuple are equal
	def equals(self, compareTuple):
		pass

	# returns a clone of self
	# attr is the schema for the tuple
	def clone(self, attr):
		pass
