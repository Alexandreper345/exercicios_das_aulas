class BanckAccount():
    def __init__(self, account_number,privados_balance):
        self.privados_balance = privados_balance
        self.account_number = account_number

    def deposit (self):
        num = float(input("quanto você quer depositar: "))
        if num < 0:
            print("operação invalida")
        else:
            self.privados_balance += num
            print(f"você deposito {num} e ficou com {self.privados_balance}")
    def withdraw(self):
        num = float(input("quanto você quer sacar: "))
        if num > self._privados_balance or  num < 0:
            print("não tem como sacar")
        else:
             self.privados_balance -= num
             print(f"você sacou {num} e ficou com {self.privados_balance}") 

    @property
    def privados_balance(self):
        return self._privados_balance

    @privados_balance.setter
    def privados_balance(self , privados_balance):
        if  privados_balance > 1000:
            print("invalido")
           
        else:
            self._privados_balance = privados_balance


bank = BanckAccount('alexandre', 1000)
bank.privados_balance = 100
print(bank.deposit())
print(bank.withdraw())