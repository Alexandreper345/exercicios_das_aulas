imc = float(input("qual é o seu peso:  "))

if imc < 18.5 :
    print("abaixo do peso")
elif 18.5 >= imc < 25:
    print("peso ideal")
elif 25 >= imc <= 30:
    print("sobrepeso")
elif 30 >= imc <= 40:
    print("obesidade")
else:
    print("obesidade mórbida")