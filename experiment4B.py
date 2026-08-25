class Node:
    def __init__(self, book):
        self.book = book
        self.left = None
        self.right = None

def create():
    book = input("Enter the book (0 for no book): ")

    if book == "0":
        return None

    root = Node(book)
    print(f"Left book of {root.book}")
    root.left = create()
    print(f"Right book of {root.book}")
    root.right = create()

    return root

def preorder(root):
    if root is None:
        return

    print(root.book, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.book, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.book, end=" ")


root = create()

print("Preorder:")
preorder(root)

print("\nInorder:")
inorder(root)

print("\nPostorder:")
postorder(root)
