import random

computador = random.randint(0,5)
jogador = int(input('advinhe um numero que o computador está pensando entre 0 a 5: '))

print(f'o numero que você escolheu foi {jogador} e o número que o computador pensou foi {computador} ')

if jogador == computador:
    print("PARABÉNS")
else:
    print('você perdeu')