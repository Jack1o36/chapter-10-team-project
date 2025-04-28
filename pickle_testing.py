import pickle


def test1():
    test1 = open("test1.txt", "a")
    name = input("enter name")
    unit = input("How many")
    price = input("the cost")
    test1.write(name)
    test1.write(unit)
    test1.write(price)
    test1.close()
    
def write_coffee():
    another = 'y'
    coffee_file = open("coffee.txt", "a")
    print("Verify - writing")
    while another.lower() == "y":
        print("Enter the following coffee data:\n")
        desc = input("Description: ")
        pounds = input("Quantity (in pounds): ")
        
        coffee_file.write(desc + '\n')
        coffee_file.write(pounds + '\n')
        
        another = input("\nDo you want to enter another? (y to continue): ")
    coffee_file.close()
    print("all data saved to coffee.txt")
