class BinarySearchTree():

    def __init__(self, key=None, value=None):
        """ Initialize the tree.

        If no key provided -> nothing
        else -> create a new node for the root
        """

        if key == None:
            self.root = None
        else:
            self.root = TreeNode(key, value, None)

    def inorder(self):
        """ Return the bst inorder. """

        if self.root == None:
            return []
        else:
            return self._inorder(self.root)

    def _inorder(self, currentNode):
        """ Inorder traversal of tree.

        currentNode -- node being considered
        """
        if currentNode == None:
            return []
        else:
            ans = []
            ans += self._inorder(currentNode.leftChild)
            ans.append((currentNode.key, currentNode.value))
            ans += self._inorder(currentNode.rightChild)
            return ans

    def put(self, key, value):
        """ Insert a key value pair into the correct location. """

        if self.root == None:
            self.root = TreeNode(key, value, None)
        else:
            self._put(key, value, self.root)

    def _put(self, key, value, currentNode):
        """ Insert key, value into self. 

        currentNode -- node being considered
        """

        if key < currentNode.key:
            # insert to the left of the root
            if currentNode.leftChild != None:
                self._put(key, value, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, value, currentNode)
        elif key > currentNode.key:
            # insert to the right of the root
            if currentNode.rightChild != None:
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value, currentNode)
        else:
            # update this node
            currentNode.value = value

    def __setitem__(self, key, value):
        """ Overriding __setitem__ for style. """
        self.put(key, value)

    def get(self, key):
        """ Retrieve value of key from tree.

        Return None if the key is not present.
        """

        res = self._get(key, self.root)
        if res == None:
            return None
        else:
            return res.value

    def _get(self, key, currentNode):
        """ Get value of key.

        currentNode -- node being considered.

        Returns the node with given key.
        """

        if currentNode == None:
            return None

        if key < currentNode.key:
            # look into left subtree
            return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            # look into right subtree
            return self._get(key, currentNode.rightChild)
        else:
            return currentNode

    def __getitem__(self, key):
        """ Override [] for style. """
        return self.get(key)

    def delete(self, key):
        """ Delete a node from the tree. """

        if self.get(key) == None:
            return
        if self.root == None:
            return
        self._delete(self._get(key, self.root))

    def _delete(self, currentNode):
        """ Actual delete of node. 
        
        currentNode -- node being considered. It's children have to be taken care here itself.
        """

        # different cases considering if the node is leaf, non-leaf or root

        # if node is a root node
        if currentNode.isRoot():
            self.root = None
        # if it is a leaf node -> easiest case, simply remove the node
        elif currentNode.isLeaf():
            # remove self from parent
            if currentNode.key < currentNode.parent.key:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # handle non-leaf non-root node
        else:
            # we need to remove this node and rewire the links
            if currentNode.leftChild != None and currentNode.rightChild == None:
                # simply promote the left child
                grandparent = currentNode.parent
                grandparent.leftChild = currentNode.leftChild
                currentNode.leftChild.parent = grandparent

            elif currentNode.rightChild != None and currentNode.rightChild == None:
                # simply promote the right child
                grandparent = currentNode.parent
                grandparent.rightChild = currentNode.rightChild
                currentNode.rightChild.parent = grandparent

            else:
                # both are non None
                # we choose either the right most child of the left subtree or the leftmost child of the right subtree
                # TODO
                pass

class TreeNode():

    def __init__(self, key, value, parent):
        """ Create a new tree node. 
        
        Key has to be non None.
        parent -- Parent TreeNode
            parent = None means that the node is the root
        """

        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parent = parent

    def isLeaf(self):
        """ Return True if a leaf node. """

        if self.leftChild == None and self.rightChild == None:
            return True
        else:
            return False

    def isRoot(self):
        """ Return True if node is a root node. """
        if self.parent == None:
            return True
        else:
            return False
