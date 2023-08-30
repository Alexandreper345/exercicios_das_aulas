salario = float(input("qual o salario: "))
aumento = (salario * 15)/100
aumento10 = (salario * 10)/100
if salario > 1250:
    print(f"seu aumento é {aumento} o total de tudo é {aumento + salario}")
else:
    print(f"seu aumento {aumento10} o total de tudo é {aumento10 + salario}")