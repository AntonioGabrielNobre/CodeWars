from PySimpleGUI import PySimpleGUI as sg

# Layout 
sg.theme('Reddist')
layout = [
    [sg.Text('Bem'),sg.Input(key='bem')],
    [sg.Text('Mal'), sg.Input(key = 'mal')],
    [sg.Checkbox('Confirma os valores informados ?')],
    [sg.Button('Confirmar')]
]

# Janela
janela = sg.Window('Tela de entrada', layout)

# Ler os eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Confirmar':
        if valores['bem'] == '1' and valores['mal'] == '2':
            print('Mal ganhou')