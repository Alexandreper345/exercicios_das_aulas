carro = float(input("quantos km o carro estava: "))
multa =  (carro - 80) * 7
if carro > 80:
    print(f'você foi multado, e a sua multa é de {multa}')
else:
    print('dirige com segurança')
