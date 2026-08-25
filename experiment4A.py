class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create():
    node = int(input("Enter the value of node (0 for no node): "))

    if node == 0:
        return None

    root = Node(node)
    print(f"Left child of {root.data}")
    root.left = create()
    print(f"Right child of {root.data}")
    root.right = create()

    return root

def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")

root = create()
print("Preorder Sequence:")
preorder(root)
