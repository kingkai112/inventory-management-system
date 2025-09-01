# saving all product data back to the file
def save_product_data(products):
    try:
        product_file = open("products.txt", "w") # opening product file for writing
        for product in products:
            line = product["name"] + ", " + product["brand"] + ", "
            line += str(product["stock"]) + ", " + str(product["cost"]) + ", " # product details
            line += product["origin"]
            product_file.write(line + "\n") # write to file
        product_file.close() # close the file
    except IOError:
        print("Error: Could not save product data") # error if something goes wrong

# function for creating receipts 
def create_transaction_invoice(customer_name, transaction_type, items, total_amount):
    invoice_number = 1 # finding a invoice that does not exists
    while True:
        filename = transaction_type + "_" + customer_name + "_" + str(invoice_number) + ".txt" 
        # invoice file name 
        try:
            open(filename, "r")
            invoice_number += 1 # if exists, next number
        except FileNotFoundError:
            break
    
    try:
        invoice_file = open(filename, "w") # open the invoice file
        invoice_file.write("WeCare Beauty Store - Transaction Invoice\n") 
        invoice_file.write("Customer: " + customer_name + "\n") # invoice details
        invoice_file.write("Type: " + transaction_type.title() + "\n")
        invoice_file.write("-" * 50 + "\n")
        
        if transaction_type == "sale": # type of transaction 
            # making columns with sapcing
            header = "Product" + " " * (20 - len("Product")) + \
                     "Qty" + " " * (10 - len("Qty")) + \
                     "Free" + " " * (10 - len("Free")) + \
                     "Amount"
            invoice_file.write(header + "\n") 
            for item in items: # for each items sold 
                line = item["name"] + " " * (20 - len(item["name"])) + \
                       str(item["quantity"]) + " " * (10 - len(str(item["quantity"]))) + \
                       str(item["free"]) + " " * (10 - len(str(item["free"]))) + \
                       str(item["amount"])
                invoice_file.write(line + "\n")
        else:
            # Manual header spacing for restock
            header = "Product" + " " * (20 - len("Product")) + \
                     "Qty" + " " * (10 - len("Qty")) + \
                     "Cost" + " " * (10 - len("Cost")) + \
                     "Amount"
            invoice_file.write(header + "\n")
            for item in items: # writing each restocked items 
                line = item["name"] + " " * (20 - len(item["name"])) + \
                       str(item["quantity"]) + " " * (10 - len(str(item["quantity"]))) + \
                       str(item["cost"]) + " " * (10 - len(str(item["cost"]))) + \
                       str(item["amount"])
                invoice_file.write(line + "\n")
        
        invoice_file.write("-" * 50 + "\n")
        invoice_file.write("Total: Rs." + str(total_amount) + "\n") # total amount
        invoice_file.close()  # close the invoice file
    except IOError:
        print("Error: Could not create invoice") # if write process fails
        