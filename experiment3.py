class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class Library:
    def __init__(self):
        self.head = None

    def insert_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty!")
        else:
            print("Deleted:", self.head.book)
            self.head = self.head.next
          
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
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Delete from Beginning")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.insert_beginning(book)

    elif choice == 2:
        book = input("Enter book name: ")
        library.insert_end(book)

    elif choice == 3:
        library.delete_beginning()

    elif choice == 4:
        library.display()

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
