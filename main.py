# importing other files to run program
from operations import handle_product_sale, handle_product_restock
from read import load_products, display_product_catalog

print("Welcome to WeCare Beauty Store")

# infinite while loop to keep showing menu until exit
while True:
    print("\nMain Menu:")
    print("1. View Products")
    print("2. Sale")   # options in main menu
    print("3. Restock")
    print("4. Exit")
    
    user_choice = input("Please select an option (1-4): ")
    
    # use if elif to valid choices 
    if user_choice == "1":
        product_data = load_products()
        display_product_catalog(product_data)
    elif user_choice == "2":
        handle_product_sale()
    elif user_choice == "3":
        handle_product_restock()
    elif user_choice == "4":
        print("Thank you for using WeCare Beauty Store System!")
        break
    else: # if user inputs invalid value
        print("Invalid option. Please try again.")
      
        