# PLP Python Week 7 - Shopping List Manager

shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    print("Commands: add / remove / show / done")

    choice = input("Enter a command: ").strip().lower()

    if choice == "add":
        item = input("Enter an item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "has been added.")
        else:
            print("Item cannot be empty.")

    elif choice == "remove":
        item = input("Enter an item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "has been removed.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye!")
        break

    else:
        print("Please enter add, remove, show, or done.")