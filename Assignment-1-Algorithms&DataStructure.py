# Name: Mariyam Member
# Student ID: 100867858
# Class: Algorithms & Data Structure
# Assignment: 1

# 1. Data Management Using Fundemental Structures - linked list:

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.next = None

#  Creating a linked list of products with given details
        
class ProductList:
    def __init__(self):
        self.head = None

    def __iter__(self):
            current = self.head
            while current:
                yield current
                current = current.next

    def insert(self, product_id, name, price, category):
        new_product = Product(product_id, name, price, category)
        if not self.head:
            self.head = new_product
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_product

    def display(self):
        current = self.head
        while current:
            print(f"ID: {current.product_id}, Name: {current.name}, Price: {current.price}, Category: {current.category}")
            current = current.next

# Read product data from file and store it in linked list
            
def load_product_data(filename):
    products = ProductList()
    with open(filename, 'r') as file:
        for line in file:
            product_id, name, price, category = line.strip().split(", ")
            products.insert(int(product_id), name, float(price), category)
    return products

# Test the loading and display function

if __name__ == "__main__":
    products = load_product_data("product_data.txt")
    products.display()

# 2. Data Manipulation Operation 
    
class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.next = None

class ProductList:
    def __init__(self):
        self.head = None

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                product_id, name, price, category = line.strip().split(", ")
                self.insert(int(product_id), name, float(price), category)

# Insert: Efficientlty add new products

    def insert(self, product_id, name, price, category):
        new_product = Product(product_id, name, price, category)
        if not self.head:
            self.head = new_product
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_product

# Update: Modify existing product details

    def update(self, product_id, new_name, new_price, new_category):
        current = self.head
        while current:
            if current.product_id == product_id:
                current.name = new_name
                current.price = new_price
                current.category = new_category
                break
            current = current.next

# Delete: Remove products while preserving data structure integrity

    def delete(self, product_id):
        if not self.head:
            return

        if self.head.product_id == product_id:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        while current:
            if current.product_id == product_id:
                prev.next = current.next
                break
            prev = current
            current = current.next

# Search: Efficiently find products using key attributes (e.g., ID, Name)
            # I am using the search by ID only

    def search(self, product_id):
        current = self.head
        while current:
            if current.product_id == product_id:
                return current
            current = current.next
        return None
    
# Sorting Algorithm Implementation - Bubble Sort:

    def bubble_sort_by_price(self):
        if not self.head:
            return None

        sorted_list = ProductList()
        current = self.head
        while current:
            sorted_list.insert(current.product_id, current.name, current.price, current.category)
            current = current.next

        sorted_head = None
        while sorted_list.head:
            min_node = self._get_min_node(sorted_list)
            if not sorted_head:
                sorted_head = min_node
                sorted_tail = min_node
            else:
                sorted_tail.next = min_node
                sorted_tail = min_node
            sorted_list.delete(min_node.product_id)

        return sorted_head

    def _get_min_node(self, product_list):
        min_node = product_list.head
        current = product_list.head.next
        while current:
            if current.price < min_node.price:
                min_node = current
            current = current.next
        return min_node

# 4. Complexity Analysis

    def bubble_sort_time_complexity(self, n):
        # Best case time complexity
        best_case_operations = n - 1
        print(f"Best Case Time Complexity: O({best_case_operations})")

        # Average case time complexity
        average_case_operations = (n * (n - 1)) // 2
        print(f"Average Case Time Complexity: O({average_case_operations})")

        # Worst case time complexity
        worst_case_operations = (n * (n - 1)) // 2
        print(f"Worst Case Time Complexity: O({worst_case_operations})")

    def display(self):
        current = self.head
        while current:
            print(f"ID: {current.product_id}, Name: {current.name}, Price: {current.price}, Category: {current.category}")
            current = current.next

# Test the operations with user input
if __name__ == "__main__":
    products = ProductList()

    # Load existing product data from file
    products.load_from_file("product_data.txt")

    while True:
        print("\n1. Insert Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. Display Products")
        print("6. Display Products Sorted by Price")
        print("7. Complexity Analysis")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = int(input("Enter Product ID: "))
            name = input("Enter Product Name: ")
            price = float(input("Enter Product Price: "))
            category = input("Enter Product Category: ")
            products.insert(product_id, name, price, category)
            print("Product added successfully.")
            products.display()
        elif choice == '2':
            product_id = int(input("Enter Product ID to update: "))
            name = input("Enter new Product Name: ")
            price = float(input("Enter new Product Price: "))
            category = input("Enter new Product Category: ")
            products.update(product_id, name, price, category)
            print("Product updated successfully.")
            products.display()
        elif choice == '3':
            product_id = int(input("Enter Product ID to delete: "))
            products.delete(product_id)
            print("Product deleted successfully.")
            products.display()
        elif choice == '4':
            product_id = int(input("Enter Product ID to search: "))
            found_product = products.search(product_id)
            if found_product:
                print(f"Product found - Name: {found_product.name}, Price: {found_product.price}, Category: {found_product.category}")
            else:
                print("Product not found.")
        elif choice == '5':
            print("Products:")
            products.display()
        elif choice == '6':
            sorted_head = products.bubble_sort_by_price()
            if sorted_head:
                sorted_products = ProductList()
                sorted_products.head = sorted_head
                print("Products sorted by price:")
                sorted_products.display()
            else:
                print("No products to sort.")
        elif choice == '7':
            # Perform complexity analysis
            n = 0
            current = products.head
            while current:
                n += 1
                current = current.next
            products.bubble_sort_time_complexity(n)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
