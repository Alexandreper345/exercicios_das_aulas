from random import choice

with open('alunos.txt', 'r') as file:
    txt = file.read()
    formato  = list(map(str,txt.split('\n')))

    

def aleatorio(list):
    print(choice(list))



def add_aluno(lista):
    name = input('qual nome quer adicionar na lista: ')
    abrir = open('alunos.txt' , 'a',) 
    abrir.write('\n' + name)
    lista.append(name)
    

def remove(lista):
    delet_aluno = input('qual aluno você quer remover da lista: ')
    with open("alunos.txt", "w") as file:
        file.write("")
    lista.remove(str(delet_aluno))
    with  open("alunos.txt", "a") as ap:
        for TXT in lista :
            ap.write(TXT+"\n")

    
print('1. mostrar a lista',
      '2. mostrar um nome da lista aleatorio',
      '3. Adicionar um nome na lista',
      '4. remover um nome da lista',
      '5.exit',sep= '\n')


while True:
    press = int(input('qual a opção quer você? '))
    if press == 1:
        with open('alunos.txt', 'r') as file:
            txt = file.read()
            formato  = list(map(str,txt.split('\n')))
            for item in formato:
                print(item)
    elif press ==2:
        aleatorio(formato)
        
    elif press == 3:
        add_aluno(formato)
    elif press == 4:
        remove(formato)
    elif press == 5:
        break
    else:
        print('opção invalida')



