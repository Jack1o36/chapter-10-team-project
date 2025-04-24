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
        pass
    
    def get_cart(self, cart):
        pass
    
    def empty(self):
        pass
    