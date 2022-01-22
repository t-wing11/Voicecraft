import PySimpleGUI as gui 

gui.theme('DarkAmber')

layout = [  [gui.Text('Some text on Row 1')],
            [gui.Text('Enter something on Row 2'), gui.InputText()],
            [gui.Button('Ok'), gui.Button('Cancel')] ]

window = gui.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()