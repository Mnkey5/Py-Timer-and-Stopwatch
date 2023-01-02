import time
import PySimpleGUI as sg
from decimal import Decimal

Home = [
    [sg.Text("Nate's Timer and Stopwatch")],
    [sg.Button("Timer")],
    [sg.Button("Stopwatch")]
]


Timer = [
    [sg.Text("Timer")],
    [sg.InputText(key="timer_length"), sg.Button("Start")]
]


Stopwatch = [
    [sg.Text("Stopwatch")],
    [sg.Button("Start / Stop")]
]


startpage = sg.Window("Start", Home, margins=(400, 300))
tim = sg.Window("Timer", Timer)
sto = sg.Window("Stopwatch", Stopwatch)


while True:
    event, values = startpage.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Timer":
        # Show the timer window
        event, values = tim.read()
        if event == "Start":
            # Get the timer length from the input field
            timer_length = values["timer_length"]
            if timer_length:
                # Convert the timer length to an integer
                timer_length = int(timer_length)
                # Start the timer
                for i in reversed(range(timer_length + 1)):
                    time.sleep(1)
                    print(i)
                    if i == 0:
                        print("TIMER IS DONE")
                        break
    if event == "Stopwatch":
        x=False
        event, values = sto.read()

        # Start the stopwatch loop
            # Check for events on the stopwatch page
        if event == "Start / Stop" or x == True:
            x=True
            counter = 0
            while True:
                print(counter)
                time.sleep(0.1)
                counter = counter + Decimal('.1')
                #event, values = sto.read()
