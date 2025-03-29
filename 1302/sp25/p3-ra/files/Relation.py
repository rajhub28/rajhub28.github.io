class Relation: 

	def __init__(self,name,attributes):
		self.name = name.upper() # name of relation
		self.attributes = attributes
		self.table = [] # list of tuple objects

	# Returns True if attribute with name aname exists in relation schema;
	# False otherwise
	def attribute_exists(self, aname):
		pass

	# Returns attribute type of attribute aname; return None if not present
	def attribute_type(self, aname):
		pass

	# Set name of relation to rname
	def setName(self, rname):
		pass

	# Add tuple tup to relation; Duplicates are fine.
	def addTuple(self,tup):
		pass

	# Return String version of relation; See output of run for format.
	def __str__(self):
		pass

	# remove duplicate tuples from self
	def removeDuplicates(self):
		pass

	# returns True if Tuple t is in self, False otherwise
	def member(self, t):
		pass

	# returns union of self and r2 as a new relation
	# You may assume that self and r2 are "union-compatible", i.e.,
	# self and r2 contain same number of attributes AND the
	# corresponding data types for the attributes are the same.
	# The attribute names need not be the same. Use the attributes
	# of self for the output relation.
	def union(self, r2):
		pass

	# returns intersection of self and r2 as a new relation
	# You may assume that self and r2 are "intersect-compatible", i.e.,
	# self and r2 contain same number of attributes AND the
	# corresponding data types for the attributes are the same.
	# The attribute names need not be the same. Use the attributes
	# of self for the output relation.
	def intersect(self, r2):
		pass

	# returns difference of self and r2 as a new relation
	# You may assume that self and r2 are "minus-compatible", i.e.,
	# self and r2 contain same number of attributes AND the
	# corresponding data types for the attributes are the same.
	# The attribute names need not be the same. Use the attributes
	# of self for the output relation.
	def minus(self, r2):
		pass

