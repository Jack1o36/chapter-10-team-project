inventory = {}
prices = {}

class CashRegister:
    
    def __init__(self, item, unit, price):
        self.__item = item
        self.__unit = unit
        self.__price = price
        #self.__price = total
        #self.__cart = cart
        
    def purchase_item(self):
        inventory[self.__item] = self.__unit
        prices[self.__item] = self.__price
        return inventory, prices
    
    def get_total(self):
        total = 0
        for item in prices:
            print(f"this is item {item}")
            total += prices[item]
            print(f"this is total {total}")
        return total
    
    def get_cart(self):
        print(f"This is the inventory, {inventory}")
        return inventory
    
    def empty(self):
        inventory.clear()
        prices.clear()
        return inventory, prices
    