nascimento =  int(input("qual sua idade: "))
alistamento = 18
falta = alistamento - nascimento
if nascimento == alistamento:
    print("vai se alistar")
elif nascimento > alistamento:
    print("passou do prazo")
else:
    print(f"falta {falta} anos para se alistar")