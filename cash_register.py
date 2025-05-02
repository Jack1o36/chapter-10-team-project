

class CashRegister:
    
    def __init__(self, item, unit, price):
        self.__item = item
        self.__unit = unit
        self.__price = price
        #self.__price = total
        #self.__cart = cart
        
    def get_item(self):
        return self.__item
    
    def get_unit(self):
        return self.__unit
    
    def get_price(self):
        return self.__price