number = int(input("digite o número que você descobrir se é impar ou par:  "))
print(f'seu número digitado foi {number}')


if number % 2 == 0:
    print('seu número é par')
else:
    print('seu número é impar')