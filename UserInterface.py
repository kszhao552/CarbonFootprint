import PySimpleGUI as sg
class UserInterface:
    def __init__(self):
        self.destination = ''
        self.origin = ''

    def Interface(self):
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
                return -1
    
            if event == 'Submit':
                if values[0] == '' or values[1] == '':
                    sg.popup('Please input origin and destination')
                else:
                    self.origin = values[0]
                    self.destination = values[1]
                    window.close()
                    return 0

l = UserInterface()
l.Interface()