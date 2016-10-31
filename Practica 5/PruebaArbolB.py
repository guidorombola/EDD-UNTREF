# from btree import *
#
# arbolB = BTree(3)
# arbolB.insert("G")
# arbolB.insert("H")
# arbolB.insert("K")
# arbolB.insert("A")
# # arbolB.insert("M")
# # arbolB.insert("R")
# # arbolB.insert("W")
# # arbolB.insert("Z")
# itr = arbolB.__iter__()
# #print(itr.__next__())
# #print(itr.__next__())
#
#
# # for leaf, value in arbolB:
# #     print(leaf, value)
#
# #print(("C",5) in arbolB)
# #print(arbolB.__str__())

from BTrees.OOBTree import *

arbol = OOBTree()
arbol.insert("AA",1)
arbol.insert("AB",5)
arbol.insert("AC",6)
arbol.insert("DD",2)

for key in arbol.keys():
    if key > "AA":
        print(key)

