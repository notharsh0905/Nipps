#Implement a function to check if a binary tree is a binary search tree (BST).
#A BST is defined as: left subtree nodes < root < right subtree nodes.
#Each node has a value, left child, and right child.
#Example: valid BST -> True, invalid -> False

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if not root:
        return True
    if not (min_val < root.val < max_val):
        return False
    return (is_valid_bst(root.left, min_val, root.val) and
            is_valid_bst(root.right, root.val, max_val))

# Helper to build tree from input
def build_tree():
    val = input("Enter node value (or 'done' to finish): ")
    if val == 'done':
        return None
    node = TreeNode(int(val))
    print(f"Left child of {val}:")
    node.left = build_tree()
    print(f"Right child of {val}:")
    node.right = build_tree()
    return root if 'root' in dir() else node

root = build_tree()
print("Is valid BST:" if is_valid_bst(root) else "Is not valid BST")