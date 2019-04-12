from unittest import TestCase

from main.tree import Tree

class testtree(TestCase):

    def testinserttree(self):

        tree = Tree()
        tree.tree_insert_recursive(5)
        tree.tree_insert_recursive(4)
        tree.tree_insert_recursive(6)
        tree.tree_insert_recursive(1)
        expected_tree_left = tree.root.left.value
        expected_tree_right = tree.root.right.value
        expected_tree_left_left = tree.root.left.left.value
        # self.assertEqual(expected_tree_left,4)
        # self.assertEqual(expected_tree_right,6)
        # self.assertEqual(expected_tree_left_left,1)
        # tree.inorder_traversal(tree.root)
        # expected_tree_tolist=tree.inorder_traversal_to_list()
        # self.assertEqual(expected_tree_tolist,[1,4,5,6])
        max_element_in_tree= tree.find_max_in_tree()
        self.assertEqual(max_element_in_tree,6)




        
