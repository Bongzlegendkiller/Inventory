# Start
# Create shoe class

class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Constructor to initialize shoe attributes
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        # Returns the cost of the shoe
        return self.cost

    def get_quantity(self):
        # Returns the quantity of the shoe
        return self.quantity

    def __str__(self):
        # Returns a string representation of the shoe
        return f"Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}"


# Create an empty list to store shoe objects
shoes_list = []


def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as file:
            # Skip the first line (header)
            next(file)
            for line in file:
                # Split the line by comma
                data = line.strip().split(',')
                # Unpack the values
                country, code, product, cost, quantity = data
                # Create a new Shoe object
                data = Shoe(country, code, product, cost, quantity)
                # Add the shoe to the list
                shoes_list.append(data)
    except FileNotFoundError:
        print("File not found!")


def capture_shoes():
    # Prompt the user to enter shoe details
    country = input("Country: ")
    code = input("Code: ")
    product = input("Product: ")
    cost = input("Cost: ")
    quantity = input("Quantity: ")
    # Create a new Shoe object
    shoe = Shoe(country, code, product, cost, quantity)
    # Add the shoe to the list
    shoes_list.append(shoe)


def view_all():
    for shoe in shoes_list:
        # Print the string representation of each shoe
        print(shoe)


def re_stock():
    # Find the shoe with the lowest quantity
    lowest_quantity_shoe = min(shoes_list, key=lambda x: x.quantity)
    print("Lowest Quantity Shoe:")
    print(lowest_quantity_shoe)

    option = input("Do you want to add this quantity of shoes? (y/n): ")
    if option.lower() == 'y':
        quantity = int(input("Enter the quantity to add: "))
        # Update the quantity of the shoe
        lowest_quantity_shoe.quantity += quantity
        print("Quantity updated successfully!")
    else:
        print("Quantity not updated.")


def search_shoe():
    code = str(input("Enter the shoe code: "))
    for shoe in shoes_list:
        # Check if the shoe code matches
        if str(shoe.code).strip(" ").lower() == code.strip("").lower():
            # Return the shoe object if found
            return print(shoe)
    # Return "None" if shoe not found
    return print("Shoe not found!")

def value_per_item():
    for shoe in shoes_list:
        # Calculate the value of each shoe
        value = shoe.cost * shoe.quantity
        print(f"Product: {shoe.product}, Value: {value}")


def highest_qty():
    # Find the shoe with the highest quantity
    highest_quantity_shoe = max(shoes_list, key=lambda x: x.quantity)
    print("Product with highest quantity:")
    print(highest_quantity_shoe)


# Main menu
# Create while loop to loop through menu
while True:
    print("********************************************")
    print("----------- Sneaker Inventory ---------------")
    print("********************************************")
    print("1. Read shoes data from file")
    print("2. Capture shoe details")
    print("3. View all shoes")
    print("4. Re-stock shoes")
    print("5. Search for a shoe")
    print("6. Calculate value per item")
    print("7. Find product with highest quantity")
    print("8. Exit")
# prompt user to enter choice
    choice = input("Enter your choice 1-8: ")
# Create if statement to call and print choice .
    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("********************************************")
        print("---------Exiting Sneaker Inventory ---------")
        print("********************************************")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
# End
        