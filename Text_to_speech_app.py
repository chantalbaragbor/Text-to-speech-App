import pyttsx3
import PySimpleGUI as sg
# sg.Window(title="Text to Speech App", layout=[[]], margins=(100, 50)).read()

layout = [
        [ 
            sg.Input(key='Text'),sg.Button("Speak")
        ],
        [
            sg.Text("Select Voice Type"),
            sg.Radio(text='Male',group_id=1,key='Male',default=True),
            sg.Radio(text='Female',group_id=1,key='Female')
        ]
    ]

# Create the window
window = sg.Window("Text to Speech App", layout)
engine = pyttsx3.init()
voices = engine.getProperty('voices')


# Create an event loop
while True:
    event, values = window.read()
    print(event,values)
    if event == "Speak":
        if values['Female'] == True:
            engine.setProperty('voice', voices[1].id)
        engine.say(values['Text'])    
        engine.runAndWait()
    if event == sg.WIN_CLOSED:
        break

# for voice in voices:
#    engine.setProperty('voice', voice.id)
#    engine.say('The quick brown fox jumped over the lazy dog.')
#    print(voice)
#    engine.runAndWait()
# print(type(voices))
