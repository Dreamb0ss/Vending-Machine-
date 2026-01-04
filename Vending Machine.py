# This function simulates a vending machine
def vending_machine():

    # Dictionary that stores all items in the vending machine
    # Each item has a name, price, and stock quantity
    items = {
        "001": {"name": "Water", "price": 1.5, "stock": 20},
        "002": {"name": "Pepsi", "price": 2.0, "stock": 13},
        "003": {"name": "Coca Cola", "price": 2.0, "stock": 5},
        "004": {"name": "7 Up", "price": 4.0, "stock": 3},
        "005": {"name": "Sprite", "price": 2.0, "stock": 6},
        "006": {"name": "Cobra", "price": 2.5, "stock": 7},
        "007": {"name": "Lipton Ice Tea", "price": 3.0, "stock": 9},
        "008": {"name": "Zoi Ice Tea", "price": 3.5, "stock": 15},
        "009": {"name": "Gatorade", "price": 5.0, "stock": 4},
        "010": {"name": "Lays Chips", "price": 3.0, "stock": 6},
        "011": {"name": "Doritos", "price": 2.5, "stock": 5},
        "012": {"name": "Cheetos", "price": 3.0, "stock": 4},
        "013": {"name": "Snickers", "price": 5.0, "stock": 5},
        "014": {"name": "Twix", "price": 3.5, "stock": 2},
        "015": {"name": "Laban Milk", "price": 7.0, "stock": 9}
    }

    # Display all available items to the user
    print("Available items:")
    for code, item in items.items():
        print(f"{code}: {item['name']} - SAR {item['price']} (Stock: {item['stock']})")

    # Ask the user to insert money
    money = float(input("\nInsert money: SAR "))

    # Store inserted money as balance
    balance = money
    print(f"Current balance: SAR {balance}")

    # Loop to allow multiple purchases
    while True:

        # Ask user to enter product code
        choice = input("\nEnter product code: ")

        # Check if the entered code exists
        if choice in items:
            item = items[choice]

            # Check if the selected item is out of stock
            if item["stock"] <= 0:
                print("Sorry, item out of stock.")
                continue

            # Check if the user has enough balance
            if balance < item["price"]:
                print("Insufficient balance.")
                continue

            # Deduct item price from balance
            balance -= item["price"]

            # Reduce stock by 1 after purchase
            item["stock"] -= 1

            # Display dispensing message
            print(f"Dispensing {item['name']}. Remaining balance: SAR {balance}")

        else:
            # Message shown if product code is invalid
            print("Invalid product code.")
            continue

        # Ask user if they want to buy more items
        again = input("Buy more (y) or get change back (n)? ").lower()

        # If user chooses to stop, return remaining balance
        if again == "n":
            print("Returning change: SAR", balance)
            break

        # Handle invalid choice
        elif again != "y":
            print("Invalid choice. Returning change.")
            print("Returning change: SAR", balance)
            break


# Call the vending machine function to start the program
vending_machine()
