import unittest
from bst import BinarySearchTree

class BinarySearchTreeTestCase(unittest.TestCase):
    """ Test suite for BinarySearchTree. """

    def test_empty_bst(self):
        """ Simple bst init should return [] on traversal. """
        a = BinarySearchTree()
        self.assertTrue(a.inorder() == [])

    def test_single_element_bst_init_int(self):
        """ Inorder rep of a bst init with a single item with int key and value. """
        a = BinarySearchTree(7, 0)
        self.assertTrue(a.inorder() == [(7, 0)])

    def test_single_element_bst_init_int_str(self):
        """ Inorder rep of a bst init with a single item with int key and str value. """
        a = BinarySearchTree(7, 'Harry')
        self.assertTrue(a.inorder() == [(7, 'Harry')])

if __name__ == '__main__':
    unittest.main()
