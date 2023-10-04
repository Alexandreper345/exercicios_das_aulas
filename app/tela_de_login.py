##tela de login para abrir o arquivo de alunos.txt

import PySimpleGUI as sg 
from random import choice




layout = [

    [sg.Text('LOGIN DE ACESSO A LISTA DE ALUNO (obs: somente o abelha)')],
    [sg.Text('NOME' ), sg.InputText(key ='chave1')],
    [sg.Text('SENHA'), sg.Input(key = 'chave2')],
    [sg.Button('ENVIAR')],
    [sg.Output(key = 'MOSTRAR', size =(30, 10)) ]
]

janela = sg.Window('tela de login', layout)


while True:
    eventos , valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'ENVIAR':
        nome_certo = 'abelha'
        senha_certo = 'abelhinha'
        nome = valores['chave1']
        senha = valores['chave2']
        if  nome == nome_certo  and senha == senha_certo:
            def add_aluno(lista,add_name: str,saida):
                lista.append(add_name)
                abrir = open('app/alunos.txt' , 'a') 
                abrir.write('\n' + add_name)
                saida['PRINTAR'].update('\n'.join(lista))
            
            def randon(lista):
                with open('app/alunos.txt', 'r') as file:
                    txt = file.read()
                    formato  = list(map(str,txt.split('\n')))
                janela['PRINTAR'].update(choice(formato))



            def remove(lista, delet_aluno,saida):
                lista.remove(delet_aluno)
                with open("app/alunos.txt", "w") as file:
                    file.write(('\n'.join(lista)))
                saida['PRINTAR'].update('\n'.join(lista))

    
            largura = 60
            altura = 20

            layout =[

                [sg.Text('Mostrar a lista de alunos?'), sg.Button('1')],
                [sg.Text('Escolher um aluno aleatorio?'), sg.Button( '2')],
                [sg.Text('Adicionar um aluno na lista?'), sg.InputText(key='adicionar'),sg.Button('3')],
                [sg.Text('Remover o aluno da Lista?'), sg.InputText(key = 'remover'),sg.Button('4')],
                [sg.Output(key = 'PRINTAR', size=(largura, altura))],
                [sg.Button('Sair')]
            ]

            janela = sg.Window('Manipulação de lista de alunos', layout)
            formato = []



            while True: 
                eventos , valores = janela.read()
                if eventos == sg.WIN_CLOSED :
                    break
                
                if eventos == '1':
                    with open('app/alunos.txt', 'r') as file:
                            txt = file.read()
                            lista  = list(map(str,txt.split('\n')))
                    janela['PRINTAR'].update('\n'.join(lista))
                            
                if eventos == '2':
                    randon(janela)
                            
                if eventos == '3':
                    add_name = valores['adicionar']
                    if add_name:
                        add_aluno(formato, add_name , janela)
                if eventos == '4':
                    remove_name = valores['remover']
                    if remove_name in lista:
                        remove(lista,remove_name,janela)
        else:
            print('mentor não encontrado')
    
