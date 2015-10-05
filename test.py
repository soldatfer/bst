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

    def test_is_root(self):
        """ Check if root node is identified correctly. """
        a = BinarySearchTree(7, 'Harry')
        a[8] = 'Ron'
	self.assertTrue(a.root.isRoot())
	self.assertFalse(a._get(8, a.root).isRoot())

    def test_non_existing_delete(self):
        """ Try to delete a non existant item. """
        a = BinarySearchTree(7, 'Harry')
	a.delete(8)
	self.assertTrue(a.inorder() == [(7, 'Harry')])

    def test_root_delete(self):
        """ Try to delete the root in a single element tree. """
        a = BinarySearchTree(7, 'Harry')
	a.delete(7)
	self.assertTrue(a.inorder() == [])

    def test_leaf_delete(self):
        """ Try to delete leaf nodes. """
        a = BinarySearchTree(7, 'Harry')
        a[8] = 'Ron'
        a[9] = 'Ginny'
        a[4] = 'Hermione'
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (7, 'Harry'), (8, 'Ron'), (9, 'Ginny')])
        a.delete(9)
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (7, 'Harry'), (8, 'Ron')])
        a.delete(4)
        self.assertTrue(a.inorder() == [(7, 'Harry'), (8, 'Ron')])
        a.delete(8)
        self.assertTrue(a.inorder() == [(7, 'Harry')])

    def test_nonleaf_leftnone_delete(self):
        """ Try to delete non leaf node with no left child. """
        a = BinarySearchTree(7, 'Harry')
        a[8] = 'Ron'
        a[9] = 'Ginny'
        a[4] = 'Hermione'
        a.delete(8)
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (7, 'Harry'), (9, 'Ginny')])

    def test_nonleaf_rightnone_delete(self):
        """ Try to delete non leaf node with no right child. """
        a = BinarySearchTree(7, 'Harry')
        a[8] = 'Ron'
        a[5] = 'Ginny'
        a[4] = 'Hermione'
        a.delete(5)
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (7, 'Harry'), (8, 'Ron')])

    def test_nonleaf_delete(self):
        """ Try to delete non leaf node with both children. """
        a = BinarySearchTree(7, 'Harry')
        a[8] = 'Ron'
        a[5] = 'Ginny'
        a[4] = 'Hermione'
        a[6] = 'Neville'

        """                     7 - Harry
                             /             \  
                       5- Ginny           8 - Ron
                       /      \  
                4-Hermione    6-Neville
        """

        a.delete(7)
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (5, 'Ginny'), (6, 'Neville'), (8, 'Ron')])
        self.assertTrue(a.root.value == 'Neville')

        a[7] = 'Harry'
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (5, 'Ginny'), (6, 'Neville'), (7, 'Harry'), (8, 'Ron')])

        a.delete(6)
        self.assertTrue(a.inorder() == [(4, 'Hermione'), (5, 'Ginny'), (7, 'Harry'), (8, 'Ron')])
        self.assertTrue(a.root.value == 'Ginny')

if __name__ == '__main__':
    unittest.main()
