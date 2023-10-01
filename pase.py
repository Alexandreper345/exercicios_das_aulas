import PySimpleGUI as sg 

layout = [

    [sg.Text('quais dessas opções você quer? ')],
    [sg.Button('Opções')],
    [sg.Input('Opções')],

    [sg.Button('Enviar')]
]

janela = sg.Window('tela de opções', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    
