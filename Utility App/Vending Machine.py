#adding all the items and assigning different codes
print("Welcome to Manaar's & Momo's Vending Machine!!!")

products = {
    "A1": {"label": "Snacks - Original Lays Chips", 
           "cost": 1.95, "Remaining": 3}, #naming this product as a snack
    "A2": {"label": "Snacks - French Cheese Chips",
            "cost": 1.95, "Remaining": 1}, #naming this product as a snack
    "A3": {"label": "Snacks - Peanut Butter Crackers", 
           "cost": 3.50, "Remaining": 7}, #naming this product as a snack
    "A4": {"label": "Snacks - Masala Peanuts", 
           "cost": 3.25, "Remaining": 4}, #naming this product as a snack
    "B1": {"label": "Chocolate - Galaxy Milk Chocolate",
            "cost": 3.00, "Remaining": 3}, #naming this product as a chocolate
    "B2": {"label": "Chocolate - Snickers",
            "cost": 3.00, "Remaining": 0}, #naming this product as a chocolate
    "B3": {"label": "Chocolate - KitKat", 
           "cost": 2.00, "Remaining": 5}, #naming this product as a chocolate
    "C1": {"label": "Cookies - White Chocolate Chip Cookies",
            "cost": 3.50, "Remaining": 4}, #naming this product as a cookie
    "C2": {"label": "Cookies - Premium Chocolate Chip Cookies", 
           "cost": 5.75, "Remaining": 1}, #naming this product as a cookie
    "C3": {"label": "Cookies - Oatmeal Raisin Cookies", 
           "cost": 2.75, "Remaining": 10}, #naming this product as a cookie
    "D1": {"label": "Beverages - Mai Dubai Water", 
           "cost": 1.00, "Remaining": 2}, #naming this product as a beverage
    "D2": {"label": "Beverages - Cold Water", 
           "cost": 1.25, "Remaining": 3}, #naming this product as a beverage
    "D3": {"label": "Beverages - Zero Coca Cola", 
           "cost": 2.50, "Remaining": 5}, #naming this product as a beverage
    "D4": {"label": "Beverages - Sprite", 
           "cost": 2.50, "Remaining": 4}, #naming this product as a beverage
    "D5": {"label": "Beverages - Fanta", 
           "cost": 2.50, "Remaining": 7}, #naming this product as a beverage
    "D6": {"label": "Beverages - Redbull", 
           "cost": 9.75, "Remaining": 1}, #naming this product as a beverage
    "E1": {"label": "Coffee - Black Coffee", 
           "cost": 2.50, "Remaining": 5}, #naming this product as a coffee
    "E2": {"label": "Coffee - Iced Coffee", 
           "cost": 5.00, "Remaining": 8}, #naming this product as a coffee
    "F1": {"label": "Tea - Green Tea", 
           "cost": 2.25, "Remaining": 10}, #naming this product as a tea
    "F2": {"label": "Tea - Iced Tea", 
           "cost": 2.75, "Remaining": 0}, #naming this product as a tea
} 

# Display the products in tabular format
def menu_shown(): 
    print(f"{'Code':<5} {'Product':<40} {'Cost (AED)':<10} {'Remaining':<10}")
    print("-" * 65)
    print("\n-- What would you like to purchase? --")
    
    category_mnr = ""  # initialize current category to empty string
    for code, info in products.items():
        qtpie = code[0]  # extract the category (A, B, C, etc.)
        if qtpie != category_mnr:
            if category_mnr:  # add a line separator after the previous category
                print("-" * 65)
            category_mnr = qtpie
        print(f"{code:<5} {info['label']:<40} {info['cost']:<10.2f} {info['Remaining']:<10}")
    
    print("0. Exit")  # if the customer does not want anything they can exit by clicking on 0

def payment_transaction(cost):
    while True:
        payment_method = input("Would you like to pay by Cash or Card? (Enter 'Cash' or 'Card'): ").strip().lower()
        
        if payment_method == "cash":
            amount_inserted = 0#this makes sure that it starts with no money
            while amount_inserted < cost:#this prompt asks for the right amount until its input by the customer
                try:
                    money = float(input(f"Input coins (AED {cost - amount_inserted:.2f} remaining): "))#tells the customer how much is left to be input by them
                    amount_inserted += money#this adds to the total money that has been inserted
                except ValueError:
                    print("An error has occurred, Please use real coins.")#if the customer enters anything except integers this is printed
            return amount_inserted - cost#if the customer enters anything higher than the cost, remaining is returned
        
        elif payment_method == "card":
            print(f"Executing AED {cost:.2f} on your card... The payment was successful!!!")#tells the customer that the card is being processed
            return 0#there is no returning of change since its card
        
        else:
            print("Invalid option. Please select 'Cash' or 'Card'.")


def Dispensing_unit():
    while True:#it loops until the exit is chosen as an option
        menu_shown()#shows what is available in the menu and shows the information
        customer_choice = input("Choose a product you would like to buy (or press '0' to exit): ").upper()

        if customer_choice == "0":#if the customer choice is 0 it exits the vending machine
            print("Thank you for using Manaar's & Momo's vending machine!!!")
            break#breaks the loop and that is the end of the function
        if customer_choice not in products:
            print("Wrong Code, Please enter the right code.")#If it is a code that is not there in the menu this is printed
            continue#customer is asked to re-enter the right code

        product = products[customer_choice]#gets the information of the product that was chosen by the customer
        if product["Remaining"] == 0:
            print(f"Sorry but {product['label']} is out of stock.")#it prints this if the product chosen is out of stock
            continue#customer is asked to re-enter a code

        print(f"You selected {product['label']} for AED {product['cost']}.")#shows the cost and the product selected by the customer
        left = payment_transaction(product["cost"])#this calls the function and calculates the change
        product["Remaining"] -= 1#removes 1 from the stock of the product that was just purchased
        print(f"Releasing {product['label']}...")#shows the customer that their product is on its way
        if left > 0:#shows the user the remaining amount if any
            print(f"Returning change: AED {left:.2f}")#returns the remaining extra amount
        print("Thank you for your purchase at Manaar's & Momo's vending machine!!!\n")#the last text after the customer is done

        #asks the customer if they want tea or coffee
        if customer_choice.startswith("C"):#if the customer chooses a code that starts with c
            extra_product = input("Would you like some coffee or tea to go with your cookie? (Y/N): ").upper()#this is asked
            if extra_product == "Y":
                choice_of_drink = input("Choose a beverage you would like with your cookie - Black coffee (E1), Iced coffee (E2), Green Tea (F1), Iced tea (F2): ").upper()
                if choice_of_drink in ["E1", "E2", "F1", "F2"]:#customer is given a choice
                    beverage = products[choice_of_drink]
                    if beverage["Remaining"] > 0:
                        print(f"Adding {beverage['label']} to your additional order for AED {beverage['cost']}.")
                        left = payment_transaction(beverage["cost"])#calculate payment for the beverage
                        beverage["Remaining"] -= 1#decrease stock
                        print(f"Releasing {beverage['label']}... Thank you for your purchase at Manaar's & Momo's vending machine!!!\n")
                        if left > 0:
                            print(f"Returning change: AED {left:.2f}")#return remaining change
                    else:
                        print(f"Sorry, {beverage['label']} is out of stock.")

        elif customer_choice.startswith("E") or customer_choice.startswith("F"):#if the customer chooses a code that starts with E or F
            choice_of_cookie = input("Would you like a cookie to go with your beverage? (Y/N): ").upper()#asks the customer if they want a cookie
            if choice_of_cookie == 'Y':
                selecting_cookie = input("What cookie would you like to have with your beverage? - White Chocolate (C1), Chocolate Chip (C2), Oatmeal Raisin (C3): ").upper()
                if selecting_cookie in ["C1", "C2", "C3"]:
                    cookie = products[selecting_cookie]
                    if cookie["Remaining"] > 0:
                        print(f"Adding {cookie['label']} to your order for AED {cookie['cost']}.")
                        left = payment_transaction(cookie["cost"])#calculate payment for the cookie
                        cookie["Remaining"] -= 1#deduct stock
                        print(f"Releasing {cookie['label']}... Thank you for your purchase!")
                        if left > 0:
                            print(f"Returning change: AED {left:.2f}")#return remaining change
                    else:
                        print(f"Sorry, {cookie['label']} is out of stock.")


# Run the function to start the vending machine
Dispensing_unit()
