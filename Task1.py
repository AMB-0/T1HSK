
"""
-------------------------------------
		HEADER OF THE PROGRAM
-------------------------------------
"""

# Import Section of the code 
import random

# Constants definition section
LOWER_SIZE_BOUND = 10
UPPER_SIZE_BOUND = 10
RANDOM_TREES = 1
Id = 0


"""
-------------------------------------
	BINARY NODE CLASS DEFINITION 
-------------------------------------
"""

# Class that creates a node of a binary tree
class binary_node()	:
    # Sets the initial configuration for a binary tree
	def __init__(self):
        # A new binary tree has no left or right Child
		global Id
		Id = Id + 1
		self.Id = Id
		self.leftChild = None
		self.rightChild = None
		self.visited = False

	# Returns the left Child node
	def get_lChild(self):
		return self.leftChild

	# Returns the right Child node
	def get_rChild(self):
		return self.rightChild

	# Returns the visited status of node
	def get_visited_status(self):
		return self.visited

	# Returns the visited status of node
	def set_visited_status(self, new_status):
		self.visited = new_status

	# Creates a new left Child node
	def create_lChild(self, nodes, leftChildAbleNode, rightChildAbleNode, index):
		self.leftChild = binary_node()
		nodes.append(self.leftChild)
		del (leftChildAbleNode[index])
		leftChildAbleNode.append(self.leftChild)
		rightChildAbleNode.append(self.leftChild)
		return self.leftChild

	# Creates a new right Child node
	def create_rChild(self, nodes, leftChildAbleNode, rightChildAbleNode, index):
		self.rightChild = binary_node()
		nodes.append(self.rightChild)
		del (rightChildAbleNode[index])
		leftChildAbleNode.append(self.rightChild)
		rightChildAbleNode.append(self.rightChild)
		return self.rightChild


"""
-------------------------------------
	BINARY TREE CLASS DEFINITION 
-------------------------------------
"""

# Class that creates a random binary tree
class random_binary_tree():

	def __init__(self):
		self.nodes = self.create_randomTree()

	def create_randomTree(self):
		# We create and empty list with every node, one with the left child capables and other with the right child capables
		nodes = []
		leftChildAbleNode= []
		rightChildAbleNode= []
		index = 0

		# Generates a random number between 50 and 100 for the size of tree
		treeNodesMax = random.randint(LOWER_SIZE_BOUND,UPPER_SIZE_BOUND)

		# First, we need to create the root of the tree
		root = binary_node()

		# We add the root to the nodes list
		nodes.append(root)
		leftChildAbleNode.append(root)
		rightChildAbleNode.append(root)

		while len(nodes) < treeNodesMax:

			# If the flag is 0, then a new left child will be created else a new right child will be created
			leftRightFlag = random.randint(0,1)

			# Choose a random Node from the correspondent list
			if leftRightFlag == 0:
				index = random.randint(0,len(leftChildAbleNode)-1)
				leftChildAbleNode[index].create_lChild(nodes, leftChildAbleNode, rightChildAbleNode, index)
			elif leftRightFlag == 1:
				index = random.randint(0,len(rightChildAbleNode)-1)
				rightChildAbleNode[index].create_rChild(nodes, leftChildAbleNode, rightChildAbleNode, index)

		return nodes

		
	# Return the list with nodes of the random Tree
	def get_nodes(self):
		return self.nodes

	# Return the First node of the random Tree in inorder
	def transverse(self, root):
		nodeList = self.get_nodes()
		rootNode = root
		print(rootNode.Id)
		if rootNode.get_lChild() is not None:
			self.transverse(rootNode.get_lChild())
		if rootNode.get_rChild() is not None:
			self.transverse(rootNode.get_rChild())
		return None

"""
-------------------------------------
			MAIN PROGRAM 
-------------------------------------
"""

# Creates a list of random trees
randomTrees = []

# Creates 50 Random Trees
while len(randomTrees) < RANDOM_TREES:
	tree = random_binary_tree()
	randomTrees.append(tree)

# Prints the whole tree structure
for node in randomTrees[0].nodes:
	print ("--------------------------")
	print ("Nodo con Id %d" % node.Id)
	if node.get_lChild():
		print ("Hijo izquierdo con Id %d" % node.get_lChild().Id)
	if node.get_rChild():
		print ("Hijo derecho con Id %d" % node.get_rChild().Id)

randomTrees[0].transverse(randomTrees[0].get_nodes()[0])