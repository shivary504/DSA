queue = []
MAX = 5

while True:
    print("\nTicket Booking Counter!!!!!!")
    print("1. Add Customer")
    print("2. Serve Customer")
    print("3. Display Queue")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(queue) < MAX:
            name = input("Enter customer name: ")
            queue.append(name)
            print("Customer added successfully.")
        else:
            print("Queue is full!")

    elif choice == 2:
        if len(queue) > 0:
            print("Served:", queue.pop(0))
        else:
            print("Queue is empty!")

    elif choice == 3:
        print("Queue:", queue)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
