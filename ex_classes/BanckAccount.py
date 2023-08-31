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
        if num > 1000 or  num < 0:
            print("não tem como sacar")
        else:
             self.privados_balance -= num
             print(f"você sacou {num} e ficou com {self.privados_balance}") 

bank = BanckAccount('alexandre', 1000)

print(bank.deposit())
print(bank.withdraw())