#Acme Retail System
def main():
    #main accepts no arguements
    #main runs every program
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
            inventory_menu()
        else:
            retail_menu()
def inventory_menu():
    #inventory_menu accepts no arugements
    #it asks the users what they want to run
    #it runs the function the user wanted to run
    pass
def display_inventory():
    #display inventory accpets no arguements
    #it displays inventory.txt
    pass
def add_inventory():
    #add inventory accepts no arguements
    #you can add to the inventory
    pass
def write_inventory_data():
    #write_inventory_data accepts no arguements
    #it writes the inventory data on the dat file to save it
    pass
    
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


    
    
    

