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

    def test_simple_element_put(self):
        """ Insert simple element and test status. """
	a = BinarySearchTree()
	a.put(7, 'Harry')
        self.assertTrue(a.inorder() == [(7, 'Harry')])

    def test_simple_element_setitem(self):
        """ Setitem simple element and test status. """
	a = BinarySearchTree()
	a[7] = 'Harry'
        self.assertTrue(a.inorder() == [(7, 'Harry')])

    def test_multiple_element_put_init_empty(self):
        """ Put mulitple items into an empty bst and test inorder. """
	a = BinarySearchTree()
	a.put(7, 'Harry')
	a[8] = 'Ron'
	a.put(4, 'Hermione')
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (7, 'Harry'), (8, 'Ron')])

    def test_multiple_element_put_init_one(self):
        """ Put mulitple items into a single element bst and test inorder. """
        a = BinarySearchTree(7, 'Harry')
	a[8] = 'Ron'
	a.put(4, 'Hermione')
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (7, 'Harry'), (8, 'Ron')])

if __name__ == '__main__':
    unittest.main()
