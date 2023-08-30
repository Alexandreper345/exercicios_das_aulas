casa =  float(input("qual o salario da casa: "))
salario =  float(input("qual o salario: "))
ano =  int(input("quantos anos: "))
prestação = casa / (ano * 12)
mínimo = salario * 30 / 100

if prestação <= mínimo:
    print(" empretismo pode concedido")
else:
    print("emprestimo negado")