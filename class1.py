class Account:

    def __init__(self,ballance,holderNaame,pin):
        self.ballance = ballance
        self.pin = pin
        self.holderName = holderNaame

MyAccount = Account(10000,'Alexandre','123-0')
WandersonAccount = Account(15000,'Wanderson','321-0')
print('Info of Alexandre,s account: ',MyAccount.__dict__)
print('Info of Wanderson,s account: ',WandersonAccount.__dict__)