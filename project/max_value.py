class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_max(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.key
