import PySimpleGUI as gui 
import os
import json

#Get controls
f = open('controls.json', 'r')
controls = json.load(f)
f.close()

controlNames = []
controlKeys = []
for attr, value in controls.items():
    for val in value:
        controlNames.append(val['name'])
        controlKeys.append(val['keys'])

print(controlNames)
print(controlKeys)
        

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

box_layout = [
    [gui.Listbox(values=controlNames, select_mode='extended', key='fac', size=(60, 9),font=('Uni Sans-Trial Book',15))]
]
layout = [  [gui.Text('Voice Craft',font=('Uni Sans-Trial Book',80))],
            [gui.Column(col_layout, element_justification='left', expand_x=True)],
            [gui.Text('Choose Device',size=(12,1),font =('Uni Sans-Trial Book',25))],
            #[gui.Image(r'' + dir + '\\assets\\logo.png',size=(200,200))],
            [gui.Combo(['laptop mic','headset'],key='dest',size=(10,1))],
            [gui.Column(box_layout,element_justification='center')] ]

window = gui.Window('',layout, resizable=True, size=(700, 700))

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED: 
        break

window.close()