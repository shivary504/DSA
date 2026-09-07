class Node:
    def __init__(self, book):
        self.book = book
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def insert(self, book, position):
        new_node = Node(book)

        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position!")
            return

        new_node.next = temp.next
        temp.next = new_node

    # Delete from any position
    def delete(self, position):

        if self.head is None:
            print("Library catalog is empty!")
            return

        if position == 1:
            print("Deleted:", self.head.book)
            self.head = self.head.next
            return

        temp = self.head

        for i in range(1, position - 1):
            if temp is None:
                print("Invalid position!")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position!")
            return

        print("Deleted:", temp.next.book)

        temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("Library catalog is empty!")
            return

        temp = self.head

        print("Library Catalog:")

        while temp:
            print(temp.book, end=" -> ")
            temp = temp.next

        print("None")


library = Library()

while True:
    print("\n--- Library Catalog ---")
    print("1. Insert Book")
    print("2. Delete Book")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        position = int(input("Enter position: "))

        library.insert(book, position)

    elif choice == 2:
        position = int(input("Enter position to delete: "))

        library.delete(position)

    elif choice == 3:
        library.display()

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
