# PLP Python Week 7 - Shopping List Manager

shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    print("1. View shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "2":
        item = input("Enter the item to add: ").strip()

        if not item:
            print("The item name cannot be empty.")
        elif item in shopping_list:
            print(item, "is already on the list.")
        else:
            shopping_list.append(item)
            print(item, "has been added.")

    elif choice == "3":
        item = input("Enter the item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print(item, "was not found on the list.")

    elif choice == "4":
        print("Thank you for using the Shopping List Manager.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")