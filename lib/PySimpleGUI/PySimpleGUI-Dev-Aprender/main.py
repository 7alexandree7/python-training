import PySimpleGUI as sg 

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key='mensagem')],
]


window = sg.Window('Login com Dev Aprender', layout)


while True:
    
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'login':
        usuario = values['usuario']
        senha = values['senha']
           
        usuario_correto = 'alexandre'
        senha_correta = '020602'
        
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
        
        else:
            window['mensagem'].update('Login Invalido')