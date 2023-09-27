km = float(input('quantos km você é a sua viagem? '))
print(f'sua viagem é de {km} km')

if km <= 200:
    print(f'você vai pagar {km * 0.50}')
else:
    print(f'você vai pagar {km * 0.45}') 