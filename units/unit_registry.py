id = 0

def add_id(fn): # ====================== or add metaclass
    def wrapper(self,health,recharge):
        global id
        id+=1
        self.__setattr__('_id',id)
        fn(self,health,recharge)
    return wrapper