import PySimpleGUI as sg

# Get screen size
screenSize = sg.Window.get_screen_size()
screenWidth = screenSize[0]
screenHeight = screenSize[1]

# --LAYOUT COMPONENT--
# Button container
col1 = [ 
    [sg.Button("Play", key = "-PLAY-")], 
    [sg.Button("Quit", key = "-QUIT-")],
]
# Layout
layout = [
    [sg.Text("WORD GAME", pad=((0,0),((int)(0.03*screenHeight),(0.01*screenHeight))), font='Calibri, 20')], 
    [sg.Column(col1, element_justification = 'center')]
]


# Create the window
window = sg.Window('Word Game', layout, finalize = True, element_justification = 'c', size=((int)(screenWidth/4),(int)(screenHeight/4)), margins=(0,0))

# --EVENT LOOP--
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == "-QUIT-":
        break
    if event == "-PLAY-":
        sg.popup_ok('Ok clicked', keep_on_top=True)
# Closing the window
window.close()