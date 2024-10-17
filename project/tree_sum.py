class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_tree(root):
    if root is None:
        return 0
    return root.key + sum_tree(root.left) + sum_tree(root.right)
