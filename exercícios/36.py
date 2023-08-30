import random
iten = [ 'pedra' , 'papel' , 'tesoura']
print('''
      
    [0] pedra
    [1] papel
    [2] tesoura
   ''')
opção = int(input("qual a opção: "))

computador = random.randint(0 , 2)

if computador == 0:
    if opção == 0:
        print("empatou")
    elif opção == 1:
        print("ganhou")
    else:
        print("perdeu")
elif computador == 1:
    if opção == 0:
        print("perdeu")
    elif opção == 1:
        print("empatou")
    else:
        print("ganhou")
elif computador == 2:
    if opção == 0:
        print("ganhou")
    elif opção == 1:
        print("perdeu")
    else:
        print("empatou")


