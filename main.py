
class Product:
    def __init__(self,product_id,name,price,quantity,category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
    def show_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Category: {self.category}")
    def increase_quantity(self,amount):
        if amount > 0:
            self.quantity += amount
            print("Successfully")
        else:
            print("Invalid")
    def decrease_quantity(self,amount):
        if 0 < amount < self.quantity:
            self.quantity -= amount
            print("Successfully")
        else:
            print("Invalid")

class Warehouse:
    def __init__(self):
        self.products = []
    def add_product(self,product):
        self.products.append(product)
        print("Successfully")
    def search_product(self,product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def remove_product(self,product_id):
        product = self.search_product(product_id)

        if product is not None:
            self.products.remove(product)
            print("Successfully")
        else:
            print("Product not found")

    def show_products(self):
        if not self.products:
            print("Empty list")
        else:
            for product in self.products:
                product.show_info()
    def increase_stock(self,product_id,amount):
        product = self.search_product(product_id)
        if product is not None:
            product.increase_quantity(amount)
        else:
            print("Invalid")

    def decrease_stock(self,product_id,amount):
        product = self.search_product(product_id)
        if product is not None:
            product.decrease_quantity(amount)
        else:
            print("Invalid")

    def update_price(self,product_id,new_price):
        product = self.search_product(product_id)

        if product is not None:
            if new_price > 0:
                product.price = new_price
                print("Successfully")
            else:
                print("Invalid")
        else:
            print("Invalid")

    def low_stock(self):
        for product in self.products:
            if product.quantity < 5:
                product.show_info()

    def total_value(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        print(f"Total Value: {total}")

warehouse = Warehouse()
while True:
    print("Welcome management system")
    print()
    print("1. Add product")
    print("2. Search product")
    print("3. Remove product")
    print("4. Show products")
    print("5. Increase stock")
    print("6. Decrease stock")
    print("7. Update price")
    print("8. Low stock")
    print("9. Total value")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice")
        continue
    if choice == 1:
        try:
            product_id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            category = input("Enter product category: ")
        except ValueError:
            print("Invalid input")
            continue

        product = Product(product_id,name,price,quantity,category)
        warehouse.add_product(product)

    elif choice == 2:
        try:
            product_id = int(input("Enter product ID: "))
        except ValueError:
            print("Invalid ID")
            continue
        product = warehouse.search_product(product_id)

        if product is not None:
            product.show_info()
        else:
            print("Invalid ID")

    elif choice == 3:
        try:
            product_id = int(input("Enter product ID: "))
        except ValueError:
            print("Invalid ID")
            continue
        warehouse.remove_product(product_id)

    elif choice == 4:
        warehouse.show_products()

    elif choice == 5:
        try:
            product_id = int(input("Enter product ID: "))
            amount = int(input("Enter product amount: "))
        except ValueError:
            print("Invalid input")
            continue
        warehouse.increase_stock(product_id,amount)

    elif choice == 6:
        try:
            product_id = int(input("Enter product ID: "))
            amount = int(input("Enter product amount: "))
        except ValueError:
            print("Invalid input")
            continue
        warehouse.decrease_stock(product_id,amount)

    elif choice == 7:
        try:
            product_id = int(input("Enter product ID: "))
            new_price = int(input("Enter product new_price: "))
        except ValueError:
            print("Invalid input")
            continue
        warehouse.update_price(product_id,new_price)

    elif choice == 8:
        warehouse.low_stock()

    elif choice == 9:
        warehouse.total_value()
    elif choice == 0:
        print("Exit")
        break
    else:
        print("Invalid choice")







