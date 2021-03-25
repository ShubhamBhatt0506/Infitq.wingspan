#lex_auth_012727119215337472135
#Start writing your code here
class Flower:
    def __init__(self):
        self.__flower_name=None
        self.__price_per_kg=None
        self.__stock_available=None
    
    def validate_flower(self):
        
        if self.__flower_name.lower() in ['orchid','rose','jasmine']:
            return True
        else:
            return False
        
    def validate_stock(self,required_quantity):
        if required_quantity>self.__stock_available:
            return False
        else:
            return True
        
    def sell_flower(self,required_quantity):
        if self.validate_flower() and self.validate_stock(required_quantity):
            self.__stock_available-=required_quantity
        else:
            print('Invalid Flower or quantity')
        
    def check_level(self):
        if self.__flower_name.lower() == 'orchid':
            if self.__stock_available<15:
                return True
            else:
                return False
        elif self.__flower_name.lower()=='rose':
            if self.__stock_available<25:
                return True
            else:
                return False
        elif self.__flower_name.lower()=='jasmine':
            if self.__stock_available<40:
                return True
            else:
                return False
        else:
            return False
        
    def set_flower_name(self,flower_name):
        self.__flower_name=flower_name
    def get_flower_name(self):
        return self.__flower_name
    
    def set_price_per_kg(self,price_per_kg):
        self.__price_per_kg=price_per_kg
    def get_price_per_kg(self):
        return self.__price_per_kg
        
    def set_stock_available(self,stock_available):
        self.__stock_available=stock_available
    def get_stock_available(self):
        return self.__stock_available
        
    
obj=Flower()
obj.set_flower_name('Rose')
print(obj.get_flower_name())
