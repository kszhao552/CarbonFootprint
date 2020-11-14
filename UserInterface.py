import PySimpleGUI as sg

layout = [ 
    [sg.Text('Origin'), sg.InputText()], 
    [sg.Text('Destination'), sg.InputText()], 
    [sg.Submit(), sg.Cancel()] 
] 

window = sg.Window('Input Locations', layout)


while True:
    event, values = window.read() 

    if event == sg.WINDOW_CLOSED:
        window.close()
        break
    
    if event == 'Submit':
        Origin = values[0]
        Destination = values[1]
        print(Origin)
        print(Destination)
        break