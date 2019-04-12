class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


class Tree:

    def __init__(self):
        self.root = None
        self.tree_list=[]

    def tree_insert(self,value):
        new_node = Node(value)

        if not self.root:
            self.root= new_node
        else:
            temp_node = self.root
            while True:
                if temp_node.value > value:
                    if not temp_node.left:
                        temp_node.left = new_node
                        break
                    else:
                        temp_node = temp_node.left
                else:
                    if temp_node.right:
                        temp_node = temp_node.right
                    else:
                        temp_node.right= new_node
                        break


    def tree_insert_recursive(self,value):
        if not self.root:
            self.root= Node(value)
        else:
             self._tree_insert_recrursive_helper(self.root,value)

    @staticmethod
    def _tree_insert_recrursive_helper(temp_root, value):
        if temp_root.value > value:
            if temp_root.left:
                Tree._tree_insert_recrursive_helper(temp_root.left,value)
            else:
                temp_root.left=Node(value)
        else:
            if temp_root.right:
                Tree._tree_insert_recrursive_helper(temp_root.right, value)
            else:
                temp_root.right=Node(value)

    def inorder_traversal(self,root):

        if root:
            self.inorder_traversal(root.left)
            print root.value
            self.inorder_traversal(root.right)

    def inorder_traversal_to_list(self):
        output_list=[]
        self.inorder_traversal_to_list_helper(self.root,output_list)
        return output_list

    @staticmethod
    def inorder_traversal_to_list_helper(root,output_list):
        if root:
            Tree.inorder_traversal_to_list_helper(root.left,output_list)
            output_list.append(root.value)
            Tree.inorder_traversal_to_list_helper(root.right,output_list)

    def find_max_in_tree(self):
        max_element=None
        return self.find_max_in_tree_helper(self.root,max_element)


    @staticmethod
    def find_max_in_tree_helper(root,max_element):
        if root:
            Tree.find_max_in_tree_helper(root.left, max_element)
            if root.value > max_element:
                print root.value,max_element
                max_element = root.value
                print max_element
            Tree.find_max_in_tree_helper(root.right, max_element)
            print max_element
        return max_element











