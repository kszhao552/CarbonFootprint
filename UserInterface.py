import PySimpleGUI as sg
class UserInterface:
    def __init__(self):
        self.destination = ''
        self.origin = ''
        self.fuelEconomy = 0
        self.Diesel = None

    def Interface(self):
        layout = [ 
            [sg.Text('Origin'), sg.InputText()], 
            [sg.Text('Destination'), sg.InputText()],
            [sg.Text('Fuel Economy'), sg.InputText()],
            [sg.Radio('Diesel', 1, key='-IN-', default = True), sg.Radio('Unleaded', 1)],
            [sg.Submit(), sg.Cancel()] 
        ] 

        window = sg.Window('Input Locations', layout)


        while True:
            event, values = window.read() 

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                window.close()
                return -1
    
            if event == 'Submit':
                if values[0] == '' or values[1] == '' or values[2] == '':
                    sg.popup('Please input origin and destination and fuel economy')
                else:          
                    try:
                        self.origin = values[0]
                        self.destination = values[1]
                        self.fuelEconomy = float(values[2])
                        self.diesel = values['-IN-']
                        sg.popup(self.diesel)
                        window.close()
                        return 0

                    except ValueError:
                        sg.popup('Fuel economy not number')

l = UserInterface()
l.Interface()



