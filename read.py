# loading products from products.txt
def load_products():
    product_list = [] # initialized an empty list
    try:
        product_file = open("products.txt", "r") # open products file
        for product_line in product_file: # read each lines
            cleaned_line = product_line.replace("\n", "")
            if cleaned_line != "": # only use non empty lines
                product_data = cleaned_line.split(", ")
                # making a product distionary
                product_dict = { 
                    "name": product_data[0],
                    "brand": product_data[1],
                    "stock": int(product_data[2]), # product details
                    "cost": int(product_data[3]),
                    "origin": product_data[4]
                }
                product_list.append(product_dict) # adding to list
        product_file.close() # closing the file
    except FileNotFoundError:
        print("Error: Product database not found") # if file is missing
    return product_list # throw back full product list

def display_product_catalog(products): # showing all products 
    print("\nWeCare Beauty Products Catalog")
    print("=" * 70) # writing = 70 times
    # making the table
    header = "Product" + " " * (20 - len("Product")) + \
             "Brand" + " " * (15 - len("Brand")) + \
             "Stock" + " " * (10 - len("Stock")) + \
             "Price" + " " * (10 - len("Price")) + \
             "Origin"
    print(header)
    print("-" * 70)
    
    for product in products: # arranging products 
        price = product["cost"] * 2
        product_line = product["name"] + " " * (20 - len(product["name"])) + \
                       product["brand"] + " " * (15 - len(product["brand"])) + \
                       str(product["stock"]) + " " * (10 - len(str(product["stock"]))) + \
                       str(price) + " " * (10 - len(str(price))) + \
                       product["origin"]
        print(product_line)
        