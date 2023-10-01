from random import choice
import PySimpleGUI as sg

with open('meu_primeiro_projeto_codigo/alunos.txt', 'r') as file:
    txt = file.read()
    formato  = list(map(str,txt.split('\n')))

    

def aleatorio(list):
    print(choice(list))



def add_aluno(lista):
    name = input('qual nome quer adicionar na lista: ')
    abrir = open('meu_primeiro_projeto_codigo/alunos.txt' , 'a',) 
    abrir.write('\n' + name)
    lista.append(name)
    

def remove(lista):
    delet_aluno = input('qual aluno você quer remover da lista: ')
    with open("meu_primeiro_projeto_codigo/alunos.txt", "w") as file:
        file.write("")
    lista.remove(str(delet_aluno))
    with  open("alunos.txt", "a") as ap:
        for TXT in lista :
            ap.write(TXT+"\n")


layout = [

    [sg.Button('Opção'),sg.Input(key= '1')],
    [sg.Button('Enviar')]
]
janela = sg.Window('tela de opções', layout)


while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Opção':
        print('1. mostrar a lista',
    '2. mostrar um nome da lista aleatorio',
    '3. Adicionar um nome na lista',
    '4. remover um nome da lista',sep= '\n')
        
    if eventos == 'Enviar':
        if valores['1'] == '1':
            with open('meu_primeiro_projeto_codigo/alunos.txt', 'r') as file:
                txt = file.read()
                formato  = list(map(str,txt.split('\n')))
                for item in formato:
                    print(item)
        if valores['1'] == '2':
            aleatorio(formato)
        if valores['1'] == '3':
            add_aluno(formato)
        if valores['1'] == '4':
            remove(formato)
        