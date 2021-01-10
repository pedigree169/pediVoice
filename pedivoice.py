#This code is done by Mukuldeb Rakshit
#pediVoice by ur_pedigree

import speech_recognition as mdr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=mdr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with mdr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'pedivoice' in command:
                command=command.replace('pedivoice','')
                print(command)
    except:
        pass
    return command

def run_pediVoice():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'search' in command:
        person=command.replace('search','')
        info=wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say it again.')

while True:
    run_pediVoice()
