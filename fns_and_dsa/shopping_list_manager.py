def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("What item do you want to add?: ")
            print(f"Added '{item}' to shopping list")
            shopping_list.append(item)
        elif choice == '2':
            # Prompt for and remove an item
            item = input("What item would you like to remove?: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        elif choice == '3':
            # Display the shopping list
            for i in shopping_list:
                print(i)
                if not shopping_list:
                    print("Shopping list is empty")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()