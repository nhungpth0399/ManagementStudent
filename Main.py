import Management


def display_menu():
    print("---------------------------------")
    print(" Student Management System")
    print("---------------------------------")
    print("1. Create New Student")
    print("2. View Details of All Students")
    print("3. Search Details of A Student")
    print("4. Update Details of Student")
    print("5. Delete Details of Student")
    print("6. Total Number of Good Student")
    print("7. Quit")

while True:
    display_menu()

    choice = int(input("Enter your choice: "))
    if choice == 1:
        Management.create_student()
    elif choice == 2:
        Management.view_students()
    elif choice == 3:
        Management.search_student()
    elif choice == 4:
        Management.update_student()
    elif choice == 5:
        Management.delete_student()
    elif choice == 6:
        Management.good_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")