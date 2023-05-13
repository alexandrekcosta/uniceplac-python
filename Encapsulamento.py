class Account:
    def __init__(self,holder,ballance,pin):
        self.__holder = holder
        self.__ballance = ballance
        self.__pin = pin

    def statement(self):
        print('Balance of ',self.__ballance,' belongs to ',self.__holder)

    def deposit(self,value):
        if(value<0):
            print('Invalid input')
        else:
            self.__ballance = self.__ballance + value

    def withdraw(self,value):

        if(self.__ballance<value):
            print('Not enough balance')
        else:
            self.__ballance = self.__ballance - value


    @property
    def balance(self):
        return self.__ballance

    @balance.setter
    def balance(self,balance):
        if(balance<0):
            print('Invalid input')
        else:
            self.__ballance = balance

Roshni = Account('Roshni',0,'111-2')
Roshni.deposit(50000)
Roshni.withdraw(1000)
Roshni.statement()
print('Info of Roshni,s account: ',Roshni.__dict__)
print('Balance: ',Roshni.balance)