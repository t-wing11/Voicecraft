import PySimpleGUI as gui 
import os
import json
import random
import string

#Get controls
f = open('controls.json', 'r')
controls = json.load(f)
f.close()

controlNames = []
controlKeys = []
controlMovement = []
for attr, value in controls.items():
    for val in value:
        controlNames.append(val['name'])
        controlKeys.append(val['keys'])
        controlMovement.append(val['movement'])

dir = os.getcwd()

#Create custom theme and add to the list of themes
gui.theme_add_new('CustomTheme', {'BACKGROUND': '#292929',
                'TEXT': '#fff4c9',
                'INPUT': '#c7e78b',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#c7e78b',
                'BUTTON': ('white', '#709053'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0})

#Set options and theme
gui.set_options(font=("Uni Sans-Trial Book", 35))
gui.theme('CustomTheme')

col_layout = [
    [gui.Button('Start', size=(20, 2), visible=True, font=('Uni Sans-Trial Book', 20))]
]

top = ["Controls","Key","Movement"]

def make_table(num_rows, num_cols):
    data = [[],[],[],[],[],[],[],[],[],[],[]]
    for i, item in enumerate(controlNames):
        if (controlMovement[i] == ""):
            controlMovement[i]="           "
        data[i+1] = [item, controlKeys[i], controlMovement[i]]
    return data
    

# ------ Make the Table Data ------
data = make_table(len(controlNames), 3)
headings = [(top[x]) for x in range(len(top))]

layout = [  [gui.Push(),gui.Text('Voice Craft',font=('Uni Sans-Trial Book',80),justification='center'),gui.Push()],
            [gui.Column(col_layout, element_justification='left', expand_x=True)],
            [gui.Text('Choose Device',size=(12,1),font =('Uni Sans-Trial Book',25))],
            [gui.Combo(['Laptop Mic','Headset'],default_value='Laptop Mic',key='device',size=(10,1))],
            [gui.Button('Select', size=(10, 1), visible=True, font=('Uni Sans-Trial Book', 10))],
            [gui.Push(),gui.Table(values=data[1:], headings=headings,size=(150,150),max_col_width=15,font=('Uni Sans-Trial Book',20),
                    justification='center',auto_size_columns=True,
                    num_rows=5,
                    alternating_row_color='#505050',
                    key='table',enable_events=True,
                    row_height=40),gui.Push()] ]

window = gui.Window('',layout, resizable=True, size=(700, 700))

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED: 
        break
    if event in ('Start'):
        print('started running')
    if event in ('Select'):
        combo = values['device']  # use the combo key
        print(combo)
    if event == 'table':
        data_selected = [data[row] for row in values[event]]
        print(data_selected[0])

window.close()