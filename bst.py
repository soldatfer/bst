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
