class bank:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.__account_number = account_number
        self.__balance = balance
    
    def getter(self):
        print(self.name)
        print(self.__account_number)
        print(self.__balance)

    def setter(self,new_balance):
        self.__balance = new_balance


customer_1 = bank("Prasanth",1,1000)

customer_1.getter()

customer_1.balance = 6000

print("After change")
customer_1.getter()

print("After setter")

customer_1.setter(7000)
customer_1.getter()