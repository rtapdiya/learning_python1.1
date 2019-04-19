from tree import Tree

def is_same_bst(tree1, tree2):
    return is_same_bst_helper(tree1.root, tree2.root)

def is_same_bst_helper(root1, root2):
    if not (root1 and root2):
        return False
    elif not root1 and root2:
        return False
    elif not root2 and root1:
        return False
    else:
        if root1.value == root2.value:
            is_same_root = True
        else:
            is_same_root = False
        is_same_left = is_same_bst_helper(root1.left, root2.left)
        is_same_right = is_same_bst_helper(root2.right, root2.right)
        print is_same_root,is_same_left,is_same_right
    return (is_same_root and is_same_left and is_same_right)


tree1= Tree()
tree2 = Tree()
tree1.tree_insert(8)
tree1.tree_insert(5)
# tree1.tree_insert(4)
# tree1.tree_insert(6)
tree1.tree_insert(11)
# tree1.tree_insert(9)
# tree1.tree_insert(12)
tree2.tree_insert(8)
tree2.tree_insert(5)
# tree2.tree_insert(4)
# tree2.tree_insert(6)
tree2.tree_insert(11)
# tree2.tree_insert(9)
# tree2.tree_insert(12)
tree1.inorder_traversal(tree1.root)
tree1.inorder_traversal(tree2.root)
print is_same_bst(tree1, tree2)




