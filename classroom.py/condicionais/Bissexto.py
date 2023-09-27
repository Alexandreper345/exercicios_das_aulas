ano = int(input('qual o ano que você quer saber se foi bissexto ou não: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano é bissexto')

else:
    print('o ano não é bissexto')

