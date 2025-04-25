class Retail_item:
    
    def __init__(self, item, unit, price):
        self.__item = item
        self.__unit = unit
        self.__price = price
        
    def set_item(self, item):
        self.__item = item
        
    def set_unit(self, unit):
        self.__unit = unit
        
    def set_price(self, price):
        self.__price = price
        
    def get_item(self):
        return self.__item
    
    def get_unit(self):
        return self.__unit
    
    def get_price(self):
        return self.__price