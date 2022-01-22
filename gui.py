import PySimpleGUI as gui 

CustomTheme = {'BACKGROUND': '#292929',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('white', '#709053'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

gui.theme_add_new('CustomTheme', CustomTheme)

gui.theme('CustomTheme')

layout = [  
            [gui.Text('Some text on Row 1')],
            [gui.Text('Enter something on Row 2'), gui.InputText()],
            [gui.Button('Ok'), gui.Button('Cancel')] ]

window = gui.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()