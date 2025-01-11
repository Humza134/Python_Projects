# import uuid
# import os
# import json

# # File to store accounts
# PRODUCT_LIST = 'product_details.json'

# # Load existing accounts from file if it exists
# if os.path.exists(PRODUCT_LIST):
#     try:
#         with open(PRODUCT_LIST, 'r') as file:
#             product_list = json.load(file)
#     except json.JSONDecodeError:
#         # Handle empty or invalid JSON file
#         product_list = []
# else:
#     product_list = []


# def add_product():
#     product_name = input("Enter the product name")
#     product_price = float(input("Enter the product price"))
#     product_quantity = int(input("Enter the product quantity"))

#     return {
#         "produc_id": str(uuid.uuid4()),
#         "product_name": product_name,
#         "product_price": product_price,
#         "product_quantity": product_quantity
#     }

# # product = add_product()
# # product_list.append(product)


# # Update the quantity or price of an existing product
# def update_product():
#     product_name = input("Enter the product name: ")
#     for product in product_list:
#         if product['product_name'] == product_name:
#             new_quantity = int(input("Enter the new quantity: "))
#             new_price = float(input("Enter the new price: "))
#             product['product_quantity'] = new_quantity
#             product['product_price'] = new_price
#             # Save Update Product to file
#             with open(PRODUCT_LIST, 'w') as file:
#                 json.dump(product_list, file)
#             return product

# # Remove a product from the list
# def remove_product():
#     product_name = input("Enter the product name: ")
#     for product in product_list:
#         if product['product_name'] == product_name:
#             product_list.remove(product)
#             print(f"Product {product_name} removed successfully.")
#             with open(PRODUCT_LIST, 'w') as file:
#                 json.dump(product_list, file)

# # Display a list of all products with their details (Product ID, Name, Price, Quantity).
# def inventory(): 
#     for product in product_list:
#         print(f"Product ID: {product['produc_id']}, Name: {product['product_name']}, Price: {product['product_price']}, Quantity: {product['product_quantity']}")

# # Search product by its name
# def search_product():
#     product_name = input("Enter the product name: ")
#     for product in product_list:
#         if product['product_name'] == product_name:
#             print(f"Product ID: {product['produc_id']}, Name: {product['product_name']}, Price: {product['product_price']}, Quantity: {product['product_quantity']}")
            

# def main():
#     while True:
#         print("1. Add Product")
#         print("2. Update Product")
#         print("3. Remove Product")
#         print("4. Inventory")
#         print("5. Search Product")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             product = add_product()
#             product_list.append(product)
#             # Save Product to file
#             with open(PRODUCT_LIST, 'w') as file:
#                 json.dump(product_list, file)
#             print(f"""
#                 Proudct created Successfully
#                 Product ID is: {product['produc_id']}
#                 Product Name is: {product['product_name']}
#                 Product Price is: {product['product_price']}
#                 Product Quantity is: {product['product_quantity']}
#                 """)
#         elif choice == "2":
#             product = update_product()
#             print(f"""
#                 Proudct Updated Successfully
#                 Product ID is: {product['produc_id']}
#                 Product Name is: {product['product_name']}
#                 Product Price is: {product['product_price']}
#                 Product Quantity is: {product['product_quantity']}
#                 """)
#         elif choice == "3":
#             remove_product()
#         elif choice == "4":
#             inventory()
#         elif choice == "5":
#             search_product()
#         elif choice == "6":
#             print("Exiting...")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

import uuid
import os
import json

# Determine the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print("BASE_DIR: ", BASE_DIR)
# Path to store product details JSON file in the same directory as app.py
PRODUCT_LIST = os.path.join(BASE_DIR, 'product_details.json')

# Load existing products from file
def load_products():
    if os.path.exists(PRODUCT_LIST):
        try:
            with open(PRODUCT_LIST, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Warning: Product file is invalid. Starting with an empty product list.")
            return []
        except Exception as e:
            print(f"Error loading product file: {e}")
            return []
    return []

# Save products to file
def save_products(products):
    try:
        with open(PRODUCT_LIST, 'w') as file:
            json.dump(products, file, indent=4)
    except Exception as e:
        print(f"Error saving product file: {e}")

# Validate user input for numbers
def get_valid_number(prompt, num_type=float):
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {num_type.__name__}.")

# Add a new product
def add_product(product_list):
    product_name = input("Enter the product name: ")
    product_price = get_valid_number("Enter the product price: ", float)
    product_quantity = get_valid_number("Enter the product quantity: ", int)

    product = {
        "product_id": str(uuid.uuid4()),
        "product_name": product_name,
        "product_price": product_price,
        "product_quantity": product_quantity,
    }
    product_list.append(product)
    save_products(product_list)
    print("Product added successfully!")
    return product

# Update an existing product
def update_product(product_list):
    product_name = input("Enter the product name to update: ")
    for product in product_list:
        if product['product_name'] == product_name:
            print("Product found. Please enter new details.")
            product['product_quantity'] = get_valid_number("Enter the new quantity: ", int)
            product['product_price'] = get_valid_number("Enter the new price: ", float)
            save_products(product_list)
            print("Product updated successfully!")
            return
    print("Product not found.")

# Remove a product
def remove_product(product_list):
    product_name = input("Enter the product name to remove: ")
    for product in product_list:
        if product['product_name'] == product_name:
            product_list.remove(product)
            save_products(product_list)
            print(f"Product '{product_name}' removed successfully.")
            return
    print("Product not found.")

# Display all products
def inventory(product_list):
    if not product_list:
        print("No products available.")
        return
    for product in product_list:
        print(f"Product ID: {product['product_id']}, Name: {product['product_name']}, "
              f"Price: {product['product_price']}, Quantity: {product['product_quantity']}")

# Search for a product by name
def search_product(product_list):
    product_name = input("Enter the product name to search: ")
    for product in product_list:
        if product['product_name'] == product_name:
            print(f"Product ID: {product['product_id']}, Name: {product['product_name']}, "
                  f"Price: {product['product_price']}, Quantity: {product['product_quantity']}")
            return
    print("Product not found.")

# Main function
def main():
    product_list = load_products()
    while True:
        print("\n1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. Inventory")
        print("5. Search Product")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_product(product_list)
        elif choice == "2":
            update_product(product_list)
        elif choice == "3":
            remove_product(product_list)
        elif choice == "4":
            inventory(product_list)
        elif choice == "5":
            search_product(product_list)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
