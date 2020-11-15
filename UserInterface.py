import PySimpleGUI as sg
class UserInterface:
    def __init__(self):
        self.destination = ''
        self.origin = ''
        self.fuelEconomy = 0
        self.AirDistance = 0
        self.diesel = None
        self.kwh = 0
        self.gallonsPropane = 0
        self.cubicFeetNatGas = 0
        self.gallonsHeatOil = 0
        self.carDistance = 0

    def Interface(self):
        layout = [ 
            [sg.Text('Origin'), sg.InputText()], 
            [sg.Text('Destination'), sg.InputText()],
            [sg.Text('Air Distance Traveled in Past Year'), sg.InputText()],
            [sg.Text('Car Distance Traveled in Past Year'), sg.InputText()],
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
                        self.fuelEconomy = float(values[4])
                        self.airDistance = float(values[2])
                        self.carDistance = float(values[3])
                        self.diesel = values['-IN-']
                        window.close()
                        return 0

                    except ValueError:
                        sg.popup('Fuel economy or air distance not number')

    def SecondInterface(self):
        layout = [ 
            [sg.Text('Kilowatt Hours of Electricity'), sg.InputText()], 
            [sg.Text('Gallons of Propane'), sg.InputText()],
            [sg.Text('Natural Gas per 100 cubic feet'), sg.InputText()],
            [sg.Text('Gallons of Heating Oil'), sg.InputText()],
            [sg.Submit(), sg.Cancel()] 
        ] 

        window = sg.Window('Input Your Monthly Utility Usage', layout)



        while True:
            event, values = window.read() 

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                window.close()
                return -1
    
            if event == 'Submit':
                if values[0] == '' or values[1] == '' or values[2] == '' or values[3] == '':
                    sg.popup('Please input all of your utilities')
                else:          
                    try:
                        self.kwh = float(values[0])
                        self.gallonsPropane = float(values[1])
                        self.cubicFeetNatGas = float(values[2])
                        self.gallonsHeatOil = float(values[3])
                        window.close()
                        return 0

                    except ValueError:
                        sg.popup('One or more of your inputs is not a number, please try again')

    def ThirdInterface(self):
        layout = [ 
            [sg.Text('Origin'), sg.InputText()], 
            [sg.Text('Destination'), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
            ]
            
        window = sg.Window('Make a Trip', layout)

            
        while True:
            event, values = window.read() 

            if event == sg.WINDOW_CLOSED or event == 'Cancel':
                window.close()
                return -1
    
            if event == 'Submit':
                if values[0] == '' or values[1] == '' or values[2] == '':
                    sg.popup('Please input origin and destination and fuel economy')
                else:
                        self.origin = values[0]
                        self.destination = values[1]
                        window.close()
                        return 0