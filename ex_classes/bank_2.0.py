class bank:
    def __init__(self):
 	    self.conta_bancario = []

#criador de contas

    def novas_contas(self):
        conta = int(input("quantas contas você quer criar: "))
        for i in range(1, conta+1):
