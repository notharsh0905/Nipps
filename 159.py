#Implement a function to find the depth of a binary tree.
#The depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if not root:
        return 0
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    return max(left_depth, right_depth) + 1

# Helper to build tree from level-order input
def build_tree():
    vals = input("Enter tree values level-order (space-separated, 'null' for empty): ").split()
    if not vals or vals[0] == 'null':
        return None
    root = TreeNode(int(vals[0]))
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if vals[i] != 'null':
            node.left = TreeNode(int(vals[i]))
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] != 'null':
            node.right = TreeNode(int(vals[i]))
            queue.append(node.right)
        i += 1
    return root

root = build_tree()
print(f"Tree depth: {max_depth(root)}")