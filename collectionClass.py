class Account:

    def __init__(self,name,pin,balance):
        self.__name = name
        self.__pin = pin
        self.__balance = balance

    def statement(self):
        print('Account holder: ',self.name,'Balance: ',self.balance)

    def withdraw(self,value):
        self.balance -= value

    def deposit(self,value):
        self.balance += value

    @property
    def number(self):
        return self.__pin

myAccount = Account('Alexandre',8444,10.25)
freida = Account('Freida',7825,60000.00)
listAccount = {myAccount.number:myAccount,freida.number:freida}
print(listAccount)