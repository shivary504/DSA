stack = []

while True:
    print("\n1. Return Book")
    print("2. Process Returned Book")
    print("3. Display Returned Books")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        stack.append(book)

    elif choice == 2:
        if stack:
            print("Processed Book:", stack.pop())
        else:
            print("No books to process")

    elif choice == 3:
        if stack:
            print("Returned Books:")
            for book in reversed(stack):
                print(book)
        else:
            print("No books in stack")

    elif choice == 4:
        break

    else:
        print("Invalid choice")
