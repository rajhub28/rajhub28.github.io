from Database import *
from Relation import *
from Tuple import *

def main():
	db = Database()

	attr1 = ["SID","SNAME"]
	dom1 = ["INTEGER","VARCHAR"]
	attr = list(zip(attr1,dom1))
	r = Relation("STUDENT",attr)

	t = Tuple(attr)
	t.addComponent(1111)
	t.addComponent("Robert Adams")
	r.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1113)
	t.addComponent("Donald James")
	r.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	r.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1114)
	t.addComponent("Michael James")
	r.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1113)
	t.addComponent("Donald James")
	r.addTuple(t)

	db.addRelation(r)

	print("Before Removing Duplicates: \n"+str(r))
	r.removeDuplicates()
	print("After Removing Duplicates: \n"+str(r))

main()
