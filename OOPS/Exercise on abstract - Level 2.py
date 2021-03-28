#lex_auth_0127476569131581442582
#Start writing your code here
from abc import ABCMeta,abstractmethod
class DirectToHomeService(metaclass=ABCMeta):
    __counter=101
    def __init__(self,consumer_name):
        self.__consumer_number=DirectToHomeService.__counter
        self.__consumer_name=consumer_name
        DirectToHomeService.__counter+=1
        
    def get_consumer_number(self):
        return self.__consumer_number
    
    def get_consumer_name(self):
        return self.__consumer_name
    @abstractmethod   
    def calculate_monthly_rent(self):  
        pass
        

class BasePackage(DirectToHomeService):
    def __init__(self,consumer_name,subscription_period,base_pack_name):
        self.__base_pack_name=base_pack_name
        self.__subscription_period=subscription_period
        super().__init__(consumer_name)

    def get_base_pack_name(self):
        return self.__base_pack_name
    
    def get_subscription_period(self):
        return self.__subscription_period
        
    def validate_base_pack_name(self):
        if self.__base_pack_name not in ['Gold','Silver','Platinum']:
            self.__base_pack_name='Silver'
            print('Base Pack Name is incorrect ,set to Silver')
        
    def calculate_monthly_rent(self):
        rent=0
        discount=0
        if self.__subscription_period in range(1,25):
            self.validate_base_pack_name()
            if self.__base_pack_name=='Silver':
                rent=350
            elif self.__base_pack_name=='Gold':
                rent=440
            elif self.__base_pack_name=='Platinum':
                rent=560
            if self.__subscription_period>12:
                discount=rent
            rent=((rent*self.__subscription_period)-discount)/self.__subscription_period
            return rent
        else:
            return -1
                
obj=BasePackage('Sita',13,'Silver')  

      
