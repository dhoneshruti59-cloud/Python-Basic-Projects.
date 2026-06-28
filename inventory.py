inventory = {}
def load_inventory():
    global inventory

    try:
        file = open("inventory.txt", "r")

        for line in file:
            product_id, name, category, qty, price, reorder = line.strip().split(",")

            inventory[product_id] = {
                "name": name,
                "category": category,
                "qty": int(qty),
                "price": float(price),
                "reorder_level": int(reorder)
            }

        file.close()
    except FileNotFoundError:
        inventory = {}

def add_product():
    product_id = input("Enter Product ID: ")

    if product_id not in inventory:
        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        qty = int(input("Enter Quantity: "))
        price = float(input("Enter Price: "))
        reorder = int(input("Enter Reorder Level: "))

        inventory[product_id] = {
            "name": name,
            "category": category,
            "qty": qty,
            "price": price,
            "reorder_level": reorder
        }

        print("Product Added Successfully")
    else:
        print("Product ID Already Exists")

def stock_in():
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        qty = int(input("Enter Quantity to Add: "))
        inventory[product_id]["qty"] += qty

        print("Stock Updated Successfully")
    else:
        print("Product Not Found")

def stock_out():
    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        qty = int(input("Enter Quantity to Remove: "))

        if inventory[product_id]["qty"] >= qty:
            inventory[product_id]["qty"] -= qty
            print("Stock Removed Successfully")
        else:
            print("Insufficient Stock")
    else:
        print("Product Not Found")

def view_inventory():
    if not inventory:
        print("Inventory is Empty")
        return

    print("\nID\tName\tCategory\tQty\tPrice\tValue")

    for pid, details in inventory.items():
        value = details["qty"] * details["price"]

        print(
            pid, "\t",
            details["name"], "\t",
            details["category"], "\t",
            details["qty"], "\t",
            details["price"], "\t",
            value
        )

def low_stock_alert():
    found = False

    print("\n*** LOW STOCK PRODUCTS ***")

    for pid, details in inventory.items():
        if details["qty"] <= details["reorder_level"]:
            print(pid, "-", details["name"])
            found = True

    if not found:
        print("No Low Stock Products")

def report():
    total_products = len(inventory)

    total_value = 0
    categories = set()

    top_product = ""
    max_value = 0

    for pid, details in inventory.items():
        value = details["qty"] * details["price"]

        total_value += value
        categories.add(details["category"])

        if value > max_value:
            max_value = value
            top_product = details["name"]

    print("\n*** INVENTORY REPORT ***")
    print("Total Products :", total_products)
    print("Total Value    :", total_value)
    print("Categories     :", categories)
    print("Top Product    :", top_product)

def save_inventory():
    file = open("inventory.txt", "w")

    for pid, details in inventory.items():
        file.write(
            f"{pid},{details['name']},{details['category']},{details['qty']},{details['price']},{details['reorder_level']}\n"
        )

    file.close()

load_inventory()

while True:
    print("\n*** INVENTORY MANAGEMENT SYSTEM ***")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Save & Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        stock_in()

    elif choice == "3":
        stock_out()

    elif choice == "4":
        view_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        report()

    elif choice == "7":
        save_inventory()
        print("Data Saved Successfully...")
        print("Exiting...")
        break
    else:
        print("Invalid Choice...")