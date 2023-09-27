salario = float(input('qual o seu salário? '))

if salario > 1250:
    print(f'o seu aumento é de 10% fica então seu salario é {salario + ((salario * 10)/100)}')
else:
    print(f'o seu aumento é de 15% fica então seu salario é {salario + ((salario * 15)/100)}')