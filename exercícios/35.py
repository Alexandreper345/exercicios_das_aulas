preços = float(input("qual o preço: "))

print('''
      
    [1] à vista dinheiro/cheque 
    [2] à vista no cartão
    [3] em até 2 vezes no cartão
    [4] 3x ou mais no cartão ''')
opção = int(input("qual a opção: "))

if opção == 1:
    total = preços - (preços * 10 /100)
    print(f"será {total}")
elif opção == 2:
    total = preços - (preços * 5/100)
    print(f"será {total}")
elif opção == 3:
    total = preços
    parcela = preços/2
    print(f"vai pagar em parcela de {parcela} reais")
elif opção == 4:
    total = preços + (preços * 20 /100)
    totalpe = int(input("quantas parcelas: "))
    parcela = total / totalpe
    print(f"o resultado será {parcela} com juros")
