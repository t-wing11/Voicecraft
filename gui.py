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
gui.set_options(font=("Uni Sans-Trial Book", 35))
gui.theme('CustomTheme')

col_layout = [
    [gui.Text('')],[gui.Text('')],[gui.Text('')],[gui.Text('')],[gui.Text('')],
    [gui.Button('Start', size=(0, 0), visible=True, font=('Times New Roman', 20))]
]

layout = [  [gui.Text('Voice Craft',font=('Times New Roman',50))],
            [gui.Column(col_layout, element_justification='right', expand_x=True)] ]

window = gui.Window('',layout, size = (700,700))

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED: 
        break

window.close()