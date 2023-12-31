from random import choice
import PySimpleGUI as sg





def add_aluno(lista,add_name: str,saida):
    lista.append(add_name)
    abrir = open('meu_primeiro_projeto_codigo/alunos.txt' , 'a') 
    abrir.write('\n' + add_name)
    saida['PRINTAR'].update('\n'.join(lista))
    
    

def remove(lista, delet_aluno,saida):
    lista.remove(delet_aluno)
    with open("meu_primeiro_projeto_codigo/alunos.txt", "w") as file:
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
        with open('meu_primeiro_projeto_codigo/alunos.txt', 'r') as file:
                txt = file.read()
                formato  = list(map(str,txt.split('\n')))
        janela['PRINTAR'].update('\n'.join(formato))
                
    if eventos == '2':
        janela['PRINTAR'].update(choice(formato))
    if eventos == '3':
        add_name = valores['adicionar']
        if add_name:
            add_aluno(formato, add_name , janela)
    if eventos == '4':
        remove_name = valores['remover']
        if remove_name in formato:
            remove(formato,remove_name,janela)

janela.close()