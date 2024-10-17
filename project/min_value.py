class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def find_min(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key
