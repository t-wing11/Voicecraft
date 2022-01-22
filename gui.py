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
        
import random
import string

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

def word():
    return '   Keybind    '
def number(max_val=1000):
    return 10
#def makes_table(num_rows,num_cols):
 #   for i in range(num_rows-1):
#
 #       for j in range(num_cols-1):
            

def make_table(num_rows, num_cols):
    data =[ [1,2,3,5,3,3,3,3,3,3],[1,1,1,1,1,1,1,1,1,1] ]
    return data
    

# ------ Make the Table Data ------
data = make_table(105, 3)
headings = [str(data[0][x]) for x in range(len(data[0]))]

layout = [  [gui.Text('Voice Craft',font=('Uni Sans-Trial Book',80))],
            [gui.Column(col_layout, element_justification='left', expand_x=True)],
            [gui.Text('Choose Device',size=(12,1),font =('Uni Sans-Trial Book',25))],
            #[gui.Image(r'' + dir + '\\assets\\logo.png',size=(200,200))],
            [gui.Combo(['laptop mic','headset'],key='dest',size=(10,1))],[gui.Text('')],
            [gui.Push(),gui.Table(values=data[1:], headings=headings,size=(100,100),font=('Uni Sans-Trial Book',20),
                    justification='center',
                    num_rows=5,
                    alternating_row_color='blue',
                    key='-TABLE-',
                    row_height=40),gui.Push()] ]

window = gui.Window('',layout, resizable=True, size=(700, 700))

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED: 
        break

window.close()