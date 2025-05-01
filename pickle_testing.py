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
    
def test2():
    test2 = open("test2.dat", 'ab')
    name = input("enter name")
    unit = input("how many?")
    price = input("the cost")
    pickle.dump(name, test2)
    pickle.dump(unit, test2)
    pickle.dump(price, test2)
    test2.close()

def test2_part2():
    test2 = open("test2.dat", "rb")
    while True:
        try:
            name = pickle.load(test2)
            units = pickle.load(test2)
            price = pickle.load(test2)
            print(name)
            print(units)
            print(price)
        except EOFError:
            break
            
def test3():
    test3 = open("test3.dat", "ab")
    item = {}
    prices = {}
    name = input("name")
    units = input("units")
    price = input("price")
    item[name] = units
    prices[name] = price
    print(item)
    print(prices)
    pickle.dump(item, test3)
    pickle.dump(prices, test3)
    test3.close()
    
def test3_part2():
    test3 = open('test3.dat', "rb")
    while True:
        try:
            item = pickle.load(test3)
            prices =pickle.load(test3)
        except EOFError:
            break
    print(item)
    print(prices)
    test3.close()
    

#instantiate an object
#thing = Classname(attribute, attribute, etc..)
#this creates an object of the class named thing
#in this case, thing will have the attributes of "shirt", 12, 20
#item['shirt'] = shoes
    
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