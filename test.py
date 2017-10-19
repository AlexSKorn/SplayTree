from __future__ import print_function  # in case you are running python 2
from BST import BSTNode,BST
from splay import SplayTree
import random
import time

def main():
	#start Binary Search Tree
	bst = BST()
	timeforInsertBST =time.time()
	print("First insecd crt 50000 random nodes into an empty tree and print the tree.")
	for i in range(50000):
		n = random.randint(0, 1000000)
		bst.insert(BSTNode(n, bst.nil, bst.nil, bst.nil))
	print ("time for BST to insert", time.time()-timeforInsertBST)
	
	timeforSearchBST= time.time()
	print("\nNow do 10000 searches. ")
	count = 0
	for i in range(10000):
		n = random.randint(0, 1000000)
		if bst.search(n) == bst.nil:
			count = count +1

	print ("time for BST to search =",time.time()-timeforSearchBST)
	##print time.time()-start1, "time for BST search"
	print (count)

	timeForDeleteBST = time.time()
	print("\nNow search for & delete some nodes.")
	for i in range(1000):
		n = random.randint(0, 1000000)
		z = bst.search(n)
		if z != bst.nil:
			bst.delete(z)
	print ("time for BST delete =",time.time()-timeForDeleteBST)

	##start splay tree
	splayTree = SplayTree()
	timeforInsertSplay = time.time()
	print("\nFirst insert 50000 random nodes into an empty tree and print the tree.")
	n = random.randint(0, 1000)
	for i in range(50000):
		n = n + 1
		splayTree.insert(BSTNode(n, splayTree.nil, splayTree.nil, splayTree.nil))
	print ("time for splay to insert =", time.time()-timeforInsertSplay)
	
	timeForSearchSplay = time.time()
	print("\nNow do 10000 searches. ")
	count2 = 0
	n = random.randint(0, 1000)
	for i in range(10000):
		n = n + 1
		if splayTree.search(n) == splayTree.nil:
			count2 = count2 +1

	print ("time for splay to search =",time.time()-timeForSearchSplay)
	print (count2)

	timeForDeleteSplay = time.time()
	print("\nNow search for & delete some nodes.")
	n = random.randint(0, 1000)
	for i in range(1000):
		n = n + 1
		z = splayTree.search(n)
		if z != splayTree.nil:
			splayTree.delete(z)
	print ("time for splay delete =",time.time()-timeForDeleteSplay)

if __name__ == "__main__":
	main()