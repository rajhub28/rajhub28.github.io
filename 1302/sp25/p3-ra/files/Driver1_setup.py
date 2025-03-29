from Database import *
from Relation import *
from Tuple import *

def main():
	db = Database()

	attr1 = ["SID","SNAME","MAJOR","GPA"] 
	dom1  = ["INTEGER","VARCHAR","VARCHAR","DECIMAL"]
	attr = list(zip(attr1,dom1))
	r1 = Relation("STUDENT",attr)

	t = Tuple(attr)
	t.addComponent(1111)
	t.addComponent("Robert Adams")
	t.addComponent("Computer Science")
	t.addComponent(4.00)
	r1.addTuple(t)

	t = Tuple(attr)
	t.addComponent(1112)
	t.addComponent("Charles Bailey")
	t.addComponent("Mathematics")
	t.addComponent(3.00)
	r1.addTuple(t)

	db.addRelation(r1)

	attr2 = ["CNUM","CTITLE","DESCRIPTION","CREDITS"]
	dom2 = ["VARCHAR","VARCHAR","VARCHAR","INTEGER"]
	attr = list(zip(attr2,dom2))
	r2 = Relation("COURSE",attr)

	t = Tuple(attr)
	t.addComponent("CSC 1301")
	t.addComponent("Intro to CS I")
	t.addComponent("Java Programming and breadth topics")
	t.addComponent(4)
	r2.addTuple(t)

	t = Tuple(attr)
	t.addComponent("CSC 1302")
	t.addComponent("Intro to CS II")
	t.addComponent("In depth Java Programming and some breadth topics")
	t.addComponent(4)
	r2.addTuple(t)

	db.addRelation(r2)

	print("Database Schema: \n" + str(db))

	print("Relation r1: \n"+str(r1))
	print("Relation r2: \n"+str(r2))

main()
