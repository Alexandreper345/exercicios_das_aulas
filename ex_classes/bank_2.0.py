class Bank():
    def __init__(self, saldos = [] ,conta = []):
        self.conta = conta
        self.saldo = saldos
    
    
    def transferencia(self):
        lista = []
        trans = float(input("quanto você quer tranferir: "))
        lista.append(trans)
        if self.conta [0] == self.conta [1]:
            self.saldo -= trans
            print(f"você tranferiu a {trans} para a conta {self.conta} e seu saldo foi para {self.saldo}")


ba = Bank( 1000, conta = ['ale','alan','abelha'] )

print(ba.transferencia())

