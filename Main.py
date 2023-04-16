import pyttsx3 as pyt
from Features import GoogleSearch
from Features import YouTubeSearch
from Features import Youtube_download
from Features import Speed_test
from Features import weather
from Automations import ChromeAuto,YouTubeAuto,WindiowsAuto
import speech_recognition as sr
import pywhatkit as pywt
import datetime
import wikipedia 
import pyjokes
import time
from playsound import playsound
import winsound
from GoogleNews import GoogleNews
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
import bs4
from bs4 import BeautifulSoup as BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests
import os
import pyautogui
import speedtest

engine = pyt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voices",voices[1].id)

def Listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        Speak2("command sir")
        audio=r.listen(source)
    try:
        print("Recognizing...")
        Speak2("wait sir ")
        text=r.recognize_google(audio,language='en-in')
        print(text)
    except Exception:
        Speak2("speak again sir")
        print("network connection  error")
        return ""
    return text.lower()

def Speak(audio):
    # print("      ")
    print(f"{audio}")
    # print("      ")
    engine.say(audio)
    engine.runAndWait()


def Speak2(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    min=int(datetime.datetime.now().minute)
    pos=str(hour)+" : "+str(min)
    Speak("hello sir nice to see you again")
    if hour >=4 and hour<12:
        Speak("good morning sir ")
        Speak("its " +pos+ " in the morning")
    elif hour >= 12 and hour < 16:
        Speak("good afternoon sir")
        engine.say("its" +pos+ " in the afternoon")
    elif hour >=16 and hour<20:
        Speak("good evening sir ")
        Speak("its " +pos+ " in the evening")
    else:
        Speak("its " +pos+ " in the night")



def TaskExe():
    # os.startfile("E:\\second_4.4.rmskin")
    time.sleep(4)
    # print("Initializing Jarvis")
    Speak("initializing Jarvis")
    time.sleep(1)
    Speak("connecting to server")
    time.sleep(1)
    Speak("system going online")
    frequency =3000
    duration=400
    winsound.Beep(frequency,duration)
    time.sleep(1)
    # playsound('C:\\Users\\user\\Downloads\\sound effects\\shryder open.mp3')
    wish()
    while True:
        query=Listen()
        query = query.replace("jarvis","")
        if 'youtube' in query:
            query = query.replace("youtube","")
            query = query.replace("search","")
            query = query.replace("on","")
            query = query.replace(" ","")
            YouTubeSearch(query)
        elif 'search' in query or 'google' in query or 'tell me' in query:
            query = query.replace("search","")
            query = query.replace("on","")
            query = query.replace("google","")
            query = query.replace("tell me","")
            query = query.replace("about","")
            query = query.replace("something","")
            query = query.replace(" ","")
            GoogleSearch(query)
        # elif 'download' in query:
        #     Speak('Starting to download video')
        #     Youtube_download()
        elif 'speed' in query:
            Speak('Checking your internet speed , wait for a while')
            Speed_test()
        elif "temperature" in query or "weather" in query:
            Speak("which city forecast you want to know sir")
            r=sr.Recognizer()
            with sr.Microphone() as source:
                voice=r.listen(source)
                city = r.recognize_google(voice)
            # city=Listen() #lucnkow
            weather(city)
        elif "remember this" in query:
            engine.say("What should i remember?")
            engine.runAndWait()
            r=sr.Recognizer()
            with sr.Microphone() as source:
                voice=r.listen(source)
                data = r.recognize_google(voice)
            print(data)
            engine.say("you said me to remember " + data)
            engine.runAndWait()
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()
        elif "do you remember something" in query:
            remember = open("data.txt", "r")
            data=remember.read()
            engine.say("you said me to remember that " + data)
            print("you said me to remember that " + data)
            engine.runAndWait()
        elif 'volume up' in query:
            pyautogui.press("volumeup")
        elif 'volume down' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' in query:
            pyautogui.press("volumemute")
        elif "calculator" in query:
            subprocess.call('calc.exe')
            Speak("opening calculater")
        elif 'play some music' in query:
            music_dir = 'C:\\Users\\rosha\\Desktop\\New folder\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        # greets 
        elif "how are you" in query:
            Speak("i am fine sir , i hope you will be fine")
        elif "hello" in query:
            Speak("yes sir i am Listening")
        elif 'goodbye' in query or "go offline" in query:
            Speak("goodbye sir")
            Speak("disconnecting to server")
            Speak("going offline")
            exit()
        elif "shutdown" in query or "shut down " in query:
            hour=int(datetime.datetime.now().hour)
            pos=str(hour)
            if hour >=20 and hour<24:
                Speak("its "+pos+" in the night" )
                Speak("perhaps you are going for sleep sir")
                Speak("have a sweet dream master see you tommorow ")
            Speak('closing all Program')
            Speak('disconnecting to servers')
            Speak("shutting down system")
            os.system("shutdown /s /t 1")
        elif "awesome" in query:
            Speak('ohhh thank you sir for making me awesome')
            time.sleep(1)
            Speak("offcourse sir")
        else :
            ChromeAuto(query)
            YouTubeAuto(query)
            WindiowsAuto(query)
        
TaskExe()
# Speak("roshan")
