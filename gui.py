import PySimpleGUI as gui 
import json

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

startstop = {'text':'Start', 'colour':'green'}
audioDevices = ['laptop mic','headset']

def addToJson(name, keys, movement, group):
    f = open('controls.json', 'r')
    controls = json.load(f)
    f.close()
    controls[group].append({'name':name, 'keys':keys, 'movement':movement})
    f = open('controls.json', 'w')
    json.dump(controls, f)
    f.close()

def removeFromJson(name, group):
    f = open('controls.json', 'r')
    controls = json.load(f)
    f.close()
    for i, item in enumerate(controlNames):
        if (item == name):
            controls[group].pop(i)
    f = open('controls.json', 'w')
    json.dump(controls, f)
    f.close()

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

#Table
top = ["Controls","Key","Movement"]

data_selected = [[]]

def open_window():
    layout = [
        [gui.Push(),gui.Text("Input Phrase",font=("Uni Sans-Trial Book", 20)),gui.Input(do_not_clear=False), gui.T('Not Selected ', size=(32,1),background_color='white', key='blank1'),gui.Push()],
        [gui.Push(),gui.Text("Input Key",font=("Uni Sans-Trial Book", 20)),gui.Input(do_not_clear=False), gui.T('Not Selected ', size=(32,1),background_color='white', key='blank2'),gui.Push()],
        [gui.Push(),gui.Text("Input Movement",font=("Uni Sans-Trial Book", 20)),gui.Input(do_not_clear=False), gui.T('Not Selected ', size=(32,1),background_color='white', key='blank3'),gui.Push()],
        [gui.Button('Enter', size=(10, 1), visible=True, font=('Uni Sans-Trial Book', 10), key='submit')]
    ]
    window = gui.Window("", layout, modal=True,size=(500,300))
    choice = None
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED:
            break
        if event in ('submit'):
            print(values[0],values[1],values[2])
            break
        
    window.close()

def make_table(num_rows, num_cols):
    data = [[""]*num_cols for i in range(num_rows+1)]
    for i, item in enumerate(controlNames):
        if (controlMovement[i] == ""):
            controlMovement[i]="              "
        data[i+1] = [item, controlKeys[i], controlMovement[i]]
    return data
    

# ------ Make the Table Data ------
data = make_table(len(controlNames), 3)
headings = [(top[x]) for x in range(len(top))]

#Layout
layout = [  [gui.Push(),gui.Text('Voice Craft',font=('Uni Sans-Trial Book',80),justification='center'),gui.Push()],

            [gui.Push(),gui.Table(values=data[1:], headings=headings,size=(150,150),max_col_width=15,font=('Uni Sans-Trial Book',20),
                    justification='center',auto_size_columns=True,
                    num_rows=5,
                    alternating_row_color='#505050',
                    key='table',enable_events=True,
                    row_height=40),gui.Push()],

            [
                gui.Push(),
                gui.Button(startstop['text'], size=(20, 2), visible=True, font=('Uni Sans-Trial Book', 20), button_color=startstop['colour'], key='startstop'),
                gui.Push(),
                gui.Text('Choose Device',size=(12,1),font =('Uni Sans-Trial Book',25)),
                gui.Combo(audioDevices,key='dest',size=(10,1), font =('Uni Sans-Trial Book',20), enable_events=True),
                gui.Push(),
            ],

            [gui.Button('Add', size=(10, 1), visible=True, font=('Uni Sans-Trial Book', 15), key='adder'),
            gui.Button('Delete', size=(10, 1), visible=True, font=('Uni Sans-Trial Book', 15),button_color='red', key='delete')]

            #gui.Image(r'./assets/logo.png',size=(200,200)),gui.Frame(layout=col_layout, element_justification='left', title='')
        ]

window = gui.Window('',layout, resizable=True, size=(700, 700), icon=r'./assets/logo.ico')

while True:
    event, values = window.read()
    if event == gui.WIN_CLOSED: 
        break
    if event in ('startstop'):
        if (startstop['text'] == 'Start'):
            startstop['text'] = 'Stop'
            startstop['colour'] = 'red'
            print('started running') # Run audio program here
        else:
            startstop['text'] = 'Start'
            startstop['colour'] = 'green'
            print('stopped running') # Stop audio program here
        
        window.Element('startstop').Update(button_color=(startstop['colour']), text=startstop['text'])

    if event in ('dest'):
        combo = audioDevices.index(values['dest'])
        print(combo) # Set device here
    if event in 'table':
        data_selected = [data[row+1] for row in values[event]]
        
    if event in ('adder'):
        open_window()

    if event in ('delete'):
        print('Deleted',data_selected)    

window.close()


    