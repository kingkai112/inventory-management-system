# importing other files for functionality
from read import load_products, display_product_catalog
from write import save_product_data, create_transaction_invoice

# logic for free items scheme
def calculate_free_items(quantity):
    return quantity // 3 

# for selling products 
def handle_product_sale():
    products = load_products()
    customer_name = input("Enter customer name: ")
    cart_items = []
    transaction_total = 0
    
    while True: # infinite while loop until exit
        display_product_catalog(products) # show products
        print("\nOptions:")
        print("1. Select product by number")
        print("2. Finish transaction")
        choice = input("Enter your choice: ")
        
        if choice == "2":
            break # exit the loop
            
        try:
            product_index = int(input("Enter product number: ")) - 1
            # if product number is valid
            if product_index >= 0 and product_index < len(products):
                selected_product = products[product_index]
                quantity = int(input("Enter quantity: "))
                
                # to check if quantity is positive
                if quantity <= 0:
                    print("Quantity must be positive")
                    continue
                # to check if stock is enough    
                if quantity > selected_product["stock"]:
                    print("Not enough stock available")
                    continue
                # calculate free items and total    
                free_items = calculate_free_items(quantity)
                total_items = quantity + free_items
                amount = selected_product["cost"] * 2 * quantity
                # adding to cart
                cart_items.append({
                    "name": selected_product["name"],
                    "quantity": quantity,
                    "free": free_items, # product details
                    "amount": amount
                })
                transaction_total += amount
                selected_product["stock"] -= total_items # removing from stock
            else:
                print("Invalid product number") # invalid product
        except ValueError:
            print("Please enter valid numbers") # error if user inputs string
    
    if cart_items: # saving new stock
        save_product_data(products)
        create_transaction_invoice(customer_name, "sale", cart_items, transaction_total) 
        # invoice generation for sale process
        print("Sale completed successfully!")

# logic for restock process
def handle_product_restock(): 
    products = load_products()
    supplier_name = input("Enter supplier name: ")
    restock_items = [] # input details for product
    transaction_total = 0
    
    while True: # infinite while loop until exit
        display_product_catalog(products) 
        # displaying products
        print("\nOptions:")
        print("1. Select existing product")
        print("2. Add new product")
        print("3. Finish restock")
        choice = input("Enter your choice: ")
        
        if choice == "3":
            break # exit loop and display products
            
        try:
            if choice == "1": # logic to add existing products
                product_index = int(input("Enter product number: ")) - 1
                if product_index >= 0 and product_index < len(products): # check if the product exists
                    selected_product = products[product_index]
                    quantity = int(input("Enter quantity to add: "))
                    new_cost = input("Enter new cost (leave blank to keep current): ")
                    
                    if quantity <= 0: # check if quantity is positive
                        print("Quantity must be positive")
                        continue
                        
                    if new_cost: # update price if given
                        selected_product["cost"] = int(new_cost)
                    
                    selected_product["stock"] += quantity # add to stocks
                    amount = selected_product["cost"] * quantity
                    
                    # add to restock list
                    restock_items.append({
                        "name": selected_product["name"],
                        "quantity": quantity,
                        "cost": selected_product["cost"],
                        "amount": amount
                    })
                    transaction_total += amount # add to total bill
                else:
                    print("Invalid product number")
                    
            elif choice == "2": # if users adds new product
                new_product = {
                    "name": input("Enter product name: "),
                    "brand": input("Enter brand: "),
                    "stock": int(input("Enter initial stock: ")), # every details for new products
                    "cost": int(input("Enter cost price: ")),
                    "origin": input("Enter country of origin: ")
                }
                products.append(new_product) # add to the collection
                amount = new_product["cost"] * new_product["stock"] # total value
                
                restock_items.append({
                    "name": new_product["name"],
                    "quantity": new_product["stock"],
                    "cost": new_product["cost"],
                    "amount": amount
                })
                transaction_total += amount # total bill
                
        except ValueError:
            print("Please enter valid numbers") # error if typed in letters 
    
    if restock_items:
        save_product_data(products) # save all changes
        create_transaction_invoice(supplier_name, "restock", restock_items, transaction_total) 
        # generate invoice
        print("Restock completed successfully!")
        # restock process complete
        