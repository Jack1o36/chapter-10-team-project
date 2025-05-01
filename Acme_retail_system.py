#Acme Retail System
import pickle
import retail_item
import cash_register
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
            if password == 'a':
                while inventory_choice != '4':
                    inventory_choice = inventory_menu()
                    if inventory_choice <= 3 or inventory_choice >= 0:
                        if inventory_choice == 1:
                            display_inventory()
                        elif inventory_choice == 2:
                             inventory = add_inventory()
                        elif inventory_choice == 3:
                            write_inventory_data(inventory)
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
    infile = open('inventory.dat', 'rb')
    print("Here is the current status of the inventory: ")
    print()
    while True:
        try:
            data = pickle.load(infile)
            for object_ in data:
                item = data[object_]
                units = item.get_unit()
                price = item.get_price()
                print(f"Description: {item}")
                print(f"Unit: {units}")
                print(f"Price: {price}")
                print()
        except EOFError:
            break
    infile.close()
    
    
def add_inventory():
    #add inventory accepts no arguements
    #you can add to the inventory
    count = 0
    items = {}
    again = 'y'
    while again == 'y':
        count += 1
        item = input(f"Enter an item description: ")
        unit = input(f"Enter the number of units for {item}: ")
        price = input(f"Enter the price per unit for {item}: ")
        inventory = retail_item.Retail_item(item, unit, price)
        items[item] = inventory
        again = input("Enter another item (y/n)? ")
    return items
    inventory_menu()
    
    
def write_inventory_data(items):
    #write_inventory_data inventory
    #it writes the inventory data on the dat file to save it
    outfile = open('inventory.dat', 'wb')
    pickle.dump(items, outfile)
        
    outfile.close()
    print(f"All items have been saved onto inventory.dat.")
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
    
    
    

