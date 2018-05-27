#!/usr/bin/env python

import speech_recognition as sr
from termcolor import colored as color
import apiai
import json
from os import system
import wikipedia as wiki
from time import sleep
import webbrowser as wb


BOLD = "\033[1m"   #use to bold the text
END = "\033[0m"    #use to close the bold text
CLIENT_ACCESS_TOKEN = "2245d4ab7c99466e806c8986a18234c4"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

google_search = "https://www.google.com/search?q="
youtube_search = "https://www.youtube.com/results?search_query="
google_drive = "https://drive.google.com"
gmail = "https://mail.google.com"
try:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        system("clear")
        print(color(BOLD+"Hola!\nAsk me anything."+END,"green"))
        while True:
            audio = r.listen(source)

#       while True:     
            try:
                query = r.recognize_google(audio)
                print(color("                                                       "+ query+"\n","red"))
            except sr.UnknownValueError:
                print (color("Listening","blue"))
            except NameError:
                print (color("...................................hey what are you dreaming about!!","blue"))

   

except KeyboardInterrupt:
    print (color(BOLD+" Bye!"+END, "cyan"))
except NameError:
                print (color("...................................hey what are you dreaming about!!","blue"))

