import pywhatkit
from pywhatkit import search
import wikipedia
from pywikihow import WikiHow, search_wikihow
import os
import webbrowser as web
import pyttsx3
from time import sleep
from pytube import YouTube
from pyautogui import click
from pyautogui import hotkey
import pyperclip
import speedtest
from GoogleNews import GoogleNews
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
import bs4
from bs4 import BeautifulSoup as BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak1(audio):
    print(" ")
    print(f": {audio}")
    print(" ")
    engine.say(audio)
    engine.runAndWait()

def Download(link):
    url=YouTube(link)
    video=url.streams.first()
    video.download('C:\\Users\\rosha\\Desktop\\New folder\\Database\\Youtube\\')

def YouTubeSearch(term):
    # result = "https://www.youtube.com/results?search_query=" + term
    # web.open(result)
    Speak1("This Is What I Found on Youtube .")
    pywhatkit.playonyt(term)

def GoogleSearch(term):
    print(term)
    query=term
    query=query.replace("what is", "")
    query=query.replace("who is","")
    query=query.replace("what do you mean by","")
    query=query.replace(" ","")

    Query=str(term)
    if 'how to' in Query:
        max_result=1
        how_to_func=search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func)==1
        how_to_func[0].print()
        Speak1(how_to_func[0].summary)
    else:
        pywhatkit.search(query)
        search=wikipedia.summary(Query,2)
        Speak1(search)

def Youtube_download():
    sleep(2)
    click(x=781,y=69)
    value=hotkey('ctrl'+'c')
    value=pyperclip.paste()
    Link=str(value)
    Download(Link)
    Speak1("Video is downloaded")
    os.startfile('C:\\Users\\rosha\\Desktop\\New folder\\Database\\Youtube\\')

def Speed_test():
    speed=speedtest.Speedtest()
    up=speed.upload()
    upload=int(int(up)/800000)
    d=speed.download()
    down=int(int(d)/800000)
    Speak1(f"Your Downloading speed is {down} Mbps")
    Speak1(f"Your Uploading speed is {upload} Mbps")

def weather(city):
    search="temperature in "+str(city)
    url=f"https://www.google.com/search?q={search}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    temp=data.find("div",class_="BNeawe").text
    Speak1(f"current {search} in {temp}")
