class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

def inorder(root):
    stack = []
    current = root

    while current is not None or stack:
        
        while current is not None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end=" ")

        current = current.right

def preorder(root):
    if root is None:
        return

    stack = [root]

    while stack:
        current = stack.pop()

        print(current.data, end=" ")

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

root = None

n = int(input("Enter number of nodes: "))

for i in range(n):
    data = int(input("Enter node value: "))
    root = insert(root, data)


print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)
