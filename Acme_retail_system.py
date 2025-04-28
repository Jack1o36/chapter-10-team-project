#Acme Retail System
import pickle
import retail_item
def main():
    #main accepts no arguements
    #main runs every program
    inventory_choice = 0
    print("Please choose from the options below:")
    print("To access the inventory control system, press 1.")
    print("To access the retail store, press 2.")
    print()
    choice = int(input("Enter your choice: "))
    if choice <= 0 or choice >= 3:
        print("Invalid")
        main()
    else:
        if choice == 1:
            password = input("Enter the inventory control password: ")
            if password == 'heisenberg':
                while inventory_choice != '4':
                    inventory_choice = inventory_menu()
                    if inventory_choice <= 3 or inventory_choice >= 0:
                        if inventory_choice == 1:
                            display_inventory()
                        elif inventory_choice == 2:
                            units, prices, items = add_inventory()
                        elif inventory_choice == 3:
                            write_inventory_data(units, prices, items)
                    else:
                        print("INVALID")
                print("Bye")
            else:
                print("Invalid")
        else:
            retail_menu()
def inventory_menu():
    #inventory_menu accepts no arugements
    #it asks the users what they want to run
    #it runs the function the user wanted to run
    choice = 0
    print("Welcome to the ACME inventory control system.")
    print("Please select an action from the following:")
    print()
    print("Press 1 to display the current inventory.")
    print("Press 2 to add inventory items to the current inventory.")
    print("Press 3 to save the inventory.")
    print("Press 4 to exit.")
    inventory_choice = int(input("Select an action (1, 2, or 3. Press 4 to EXIT): "))
    return inventory_choice
    main()
def display_inventory():
    #display inventory accpets no arguements
    #it displays inventory.dat
    end_of_file = False
    infile = open('inventory.dat', 'rb')
    while not end_of_file:
        try:
            item = pickle.load(infile)
            print(item)
        except EOFError:
            end_of_file = True
    infile.close()
    
    
def add_inventory():
    #add inventory accepts no arguements
    #you can add to the inventory
    count = 0
    items = {}
    units = {}
    prices = {}
    again = 'y'
    while again == 'y':
        count += 1
        item = input(f"Enter an item description: ")
        unit = input(f"Enter the number of units for {item}: ")
        price = input(f"Enter the price per unit for {item}: ")
        inventory = retail_item.Retail_item(item, unit, price)
        classitem = inventory.get_item()
        classunit = inventory.get_unit()
        classprice = inventory.get_price()
        items[classitem] = count
        units[classitem] = classunit
        prices[classitem] = classprice
        again = input("Enter another item (y/n)? ")
    return units, prices, items
    inventory_menu()
    
    
def write_inventory_data(units, prices, items):
    #write_inventory_data inventory
    #it writes the inventory data on the dat file to save it
    count = 0
    outfile = open('inventory.dat', 'ab')
    for item in items:
        pickle.dump(item, outfile)
def retail_menu():
    pass
def display_cart():
    pass

def display_item():
    pass

def purchase_item():
    pass

def empty_cart():
    pass

def check_out():
    pass

def goto_main():
    #goto_main accepts no arguements
    #it is ran when the user wants to go back to main
    main()

main()
    
    
    

