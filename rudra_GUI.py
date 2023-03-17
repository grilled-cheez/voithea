import PySimpleGUI as sg

lq = ["a", "b"]
state = ""
ftype = "bold"  # to differentiate b/w query and response
fsize = 15  # to differentiate b/w query and response
# STEP 1 define the layout
col_1 = [
    [sg.LB(lq, font=(ftype, fsize), size=(40, 10), key="-LB-")],  # user's query
    # state of the takeCommand function (reassignment)
    [sg.Text(state, font=(None, 15), key="-ST-")],
]
col_2 = [
    [sg.Button('Start', size=(8, 1))],
    [sg.Button('Terminate', size=(8, 1))],
    [sg.Button('Mute', size=(8, 1), button_color="red")]
]

layout = [
    [sg.Col(col_1), sg.VerticalSeparator(), sg.Col(col_2)]
]


# STEP 2 - create the window
window = sg.Window('My new window', layout)

# STEP3 - the event loop
while True:
    # Read the event that happened and the values dictionary
    event, values = window.read()
    print(event, values)
    # If user closed window with X or if user clicked "Exit" button then exit
    if event == sg.WIN_CLOSED or event == 'Terminate':
        break
    if event == 'Start':
        state = "aaaa"

    if event == 'Mute':
        lq.append()
        window["-LB-"].update(lq)
window.close()
