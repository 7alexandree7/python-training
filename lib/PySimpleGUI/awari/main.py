# 1 Passo - Importar a blibioteca
import PySimpleGUI as sg

# 2 Passo - Definir Layout
layout = [
    [sg.Text('Ola, PySimpleGui')],
    [sg.Button('Click Here')]
]

# 3 Passo Crie uma instância da janela utilizando o layout definido:
window = sg.Window('Minha Primeira Interface', layout)


# 4 Passo Crie um loop para manter a janela aberta e capturar as interações do usuário:
while True:
    
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED():
        break
    
    if event == 'Click Here':
        sg.popup('Botão clicado')
    

# 5 Passo Fechar a Janela
window.close()