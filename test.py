import PySimpleGUI as sg

layout = [

    [sg.Text('add nome'), sg.Input(key = 'adicionar'), sg.Button('1')],
    [sg.Output(key = 'output' , size= (60, 30))]

]

janela = sg.Window('teste', layout)

while True:
    eventos , valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == '1':
        if valores == 'adicionar':
            print('aaaaaaaa')