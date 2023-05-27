class Worker:

    def __init__(self,name,cpf,salary):
        self._name = name
        self._cpf = cpf
        self._salary = salary

    def get_bonus(self):

        return self._salary * 0.10

class Mananger(Worker):

    def __init__(self,name,cpf,salary,password,quantity_mananged):

        super().__init__(name,cpf,salary)
        self.__password = password
        self.__quantity_mananged = quantity_mananged

    def verify(self,password):

        if self. __password == password:
            print("Access allowed")
            return True

        else:
            print("Access denied")
            return False

    def get_bonus(self):

        return self._salary * 0.15

class BonusControl:

    def __init__(self):
        self.__bonus_total = 0

    def register(self,worker):
        self.__bonus_total += worker.get_bonus()

mananger = Mananger("Ana","123",20000,"123",20)
print(mananger.__dict__)
worker = Worker("Bia","111",10500.0)
print(worker.__dict__)
control = BonusControl()
control.register(worker)
control.register(mananger)
print("Bonus value for worker: ",worker.get_bonus())
print("Bonus value for manager: ",mananger.get_bonus())
print(control.__dict__)
