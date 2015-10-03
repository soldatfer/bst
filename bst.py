class BinarySearchTree():

    def __init__(self, key=None, value=None):
        """ Initialize the tree.

        If no key provided -> nothing
        else -> create a new node for the root
        """

        if key == None:
            self.root = None
        else:
            self.root = TreeNode(key, value)

    def inorder(self):
        """ Return the bst inorder. """

        if self.root == None:
            return []
        else:
            return self.root.inorder()

    def put(self, key, value):
        """ Insert a key value pair into the correct location. """

        if self.root == None:
            self.root = TreeNode(key, value)
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
                currentNode.leftChild = TreeNode(key, value)
        elif key > currentNode.key:
            # insert to the right of the root
            if currentNode.rightChild != None:
                self._put(key, value, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, value)
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

        if self.root == None:
            return None
        else:
            return self._get(key, self.root)

    def _get(self, key, currentNode):
        """ Get value of key.

        currentNode -- node being considered.
        """

        if key < currentNode.key:
            # look into left subtree
            if currentNode.leftChild == None:
                return None
            else:
                return self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            # look into right subtree
            if currentNode.rightChild == None:
                return None
            else:
                return self._get(key, currentNode.rightChild)
        else:
            return currentNode.value

    def __getitem__(self, key):
        """ Override [] for style. """
        return self.get(key)

class TreeNode():

    def __init__(self, key, value):
        """ Create a new tree node. 
        
        Key has to be non None.
        """

        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None

    def inorder(self):
        """ Return the in order key, value pairs. """
        ans = []
        if self.leftChild != None:
            ans += self.leftChild.inorder()
        ans.append((self.key, self.value))
        if self.rightChild != None:
            ans += self.rightChild.inorder()

        return ans
