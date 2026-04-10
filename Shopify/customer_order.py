"""Main file that imports order class and customer performs order"""
import order_attr

def main():
    obj = order_attr.Order()
    order_attr.introduction()
    while True:
        print("--- MENU ---")
        print("1. Display Catalogue")
        print("2. Place Order")
        print("3. View Orders")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":

            obj.catalogue()

        elif choice == "2":
            print("Enter your name: ")
            name = str(input().strip())
            print("Enter Item name:")
            item = str(input().strip())

            print("Enter quantity:")
            quantity = int(input().strip())
            obj.place_order(name,item,quantity)

        elif choice == "3":
            print("Enter your name: ")
            name = input().strip()
            obj.display_order(name)

        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("⚠ Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()