from Database import *
from Relation import *
import sys

def main():
    db = Database()
    db.initializeDatabase(sys.argv[1])
    #print(str(db))
    r1 = db.getRelation("BAR")
    print(r1)
    r2 = db.getRelation("DRINKER")
    print(r2)
    r3 = db.getRelation("BEER")
    print(r3)
    r4 = db.getRelation("FREQUENTS")
    print(r4)
    r5 = db.getRelation("LIKES")
    print(r5)
    r6 = db.getRelation("SERVES")
    print(r6)

main()
