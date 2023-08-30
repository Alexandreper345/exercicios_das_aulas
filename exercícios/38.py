lista = []
soma = 0

for i in range(1 , 500):
    if  i % 3 == 0:
        lista.append(i)
print(lista)

for j in range(len(lista)):
    soma = soma + lista[j]
print(soma)