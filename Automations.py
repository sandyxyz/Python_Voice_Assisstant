from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep 
import pyttsx3 as pyt
import speech_recognition as sr
import webbrowser as web

engine = pyt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voices",voices[1].id)

def Speak(audio):
    # print("      ")
    # print(f"{audio}")
    # print("      ")
    engine.say(audio)
    engine.runAndWait()

def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to","")
        
        num = Tab

        bb = f'ctrl + {num}'

        press_and_release(bb)

    elif 'open' in query:

        name = query.replace("open ","")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        else:

            string = "https://www." + NameA + ".com"

            string_2 = string.replace(" ","")

            web.open(string_2)

def YouTubeAuto(command):

    query = str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')

    elif 'full screen' in query:

        press('f')

    elif 'film screen' in query:

        press('t')

    elif 'skip' in query:

        press('l')

    elif 'back' in query:

        press('j')

    elif 'increase' in query:

        press_and_release('SHIFT + .')

    elif 'decrease' in query:

        press_and_release('SHIFT + ,')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')
    
    elif 'search' in query:

        click(x=667, y=146)

        Speak("What To Search Sir ?")

        search = Speak()

        write(search)

        sleep(0.8)

        press('enter')

    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')
    

def WindiowsAuto(command):

    query = str(command)

    if 'home screen' in query:

        press_and_release('windows + m')

    elif 'minimize' in query:

        press_and_release('windows + m')

    elif 'show start' in query:

        press('windows')

    elif 'open setting' in query:

        press_and_release('windows + i')

    elif 'open search' in query:

        press_and_release('windows + s')

    elif 'screen shot' in query:

        press_and_release('windows + SHIFT + s')

    elif 'restore windows' in  query:

        press_and_release('Windows + Shift + M')
