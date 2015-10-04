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

    def test_element_get_empty(self):
        """ Get simple element."""
	a = BinarySearchTree()
        self.assertTrue(a.get(7) == None)

    def test_element_get_simple(self):
        """ Get simple element."""
	a = BinarySearchTree()
	a[7] = 'Harry'
        self.assertTrue(a.get(7) == 'Harry')

    def test_element_get_nonexistent(self):
        """ Get nonexistent element."""
	a = BinarySearchTree()
	a[7] = 'Harry'
        self.assertTrue(a[6] == None)

    def test_multiple_element_get(self):
        """ Put mulitple items into an empty bst and test inorder. """
	a = BinarySearchTree()
	a.put(7, 'Harry')
	a[8] = 'Ron'
	a.put(4, 'Hermione')
	a[9] = 'Ginny'
        self.assertTrue(a[4] == 'Hermione')

    def test_simple_leaf(self):
        """ Tree of single item. """
        a = BinarySearchTree()
        a[7] = 'Harry'
        self.assertTrue(a.root.isLeaf())

    def test_multiple_leaf(self):
        """ Tree of single item. """
        a = BinarySearchTree()
        a[7] = 'Harry'
        a[8] = 'Ron'
        a.put(4, 'Hermione')
        a[9] = 'Ginny'
        self.assertFalse(a._get(7, a.root).isLeaf())

    def test_no_parent(self):
        """ Check parent of root. """
        a = BinarySearchTree(7, 'Harry')
	self.assertTrue(a.root.parent == None)

    def test_simple_parent(self):
        """ Check parent. """
        a = BinarySearchTree(7, 'Harry')
        a[8] = 'Ron'
	self.assertTrue(a._get(8, a.root).parent.value == 'Harry')

if __name__ == '__main__':
    unittest.main()
