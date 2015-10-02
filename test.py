import unittest
from bst import BinarySearchTree

class BinarySearchTreeTestCase(unittest.TestCase):
    """ Test suite for BinarySearchTree. """

    def test_empty_bst(self):
        """ Simple bst init should return [] on traversal. """
        a = BinarySearchTree()
        self.assertTrue(a.inorder() == [])

if __name__ == '__main__':
    unittest.main()
