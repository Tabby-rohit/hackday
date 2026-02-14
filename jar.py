import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sounddevice as sd
import numpy as np


eng=pyttsx3.init("sapi5")
vic=eng.getProperty("voices")
eng.setProperty("voice",vic[1].id)
# print(vic[1].id)
def speak(aud):
    eng.say(aud)
    eng.runAndWait()
def wish():
    hr=int(datetime.datetime.now().hour)
    if hr>0 and hr<12:
        speak("good morning sir")
    elif hr>12 and hr<18:
        speak("good afternoon")
    elif hr>18 and hr<20:
        speak("good evening")    
    speak("I am yor personal assistant jarvis how may i help you") 


def viceinput():
    r = sr.Recognizer()
    
    fs = 16000
    duration = 5

    speak("listening")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    audio = sr.AudioData(recording.tobytes(), fs, 2)

    try:
        speak("recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(query)
        return query
    except:
        speak("repeat")
        return "none"

wish()
a=True
while a==True:
 query=viceinput().lower()
 if "wikipedia" in query :
    query=query.replace("wikipedia","")
    speak(f"according to wikipedia{wikipedia.summary(query,sentences=2)}")
 elif "open youtube" in query:
    webbrowser.open("youtube.com")  
 elif "close" in query:
    a=False   
 elif "open google" in query:
    webbrowser.open("google.com")
 elif "news" in query:
    webbrowser.open("https://www.bing.com/ck/a?!&&p=e7464a70a9e2ce997e7b8b1d2b00eea4d2f4faf30f60f3e1b23212063d7425f7JmltdHM9MTc0ODY0OTYwMA&ptn=3&ver=2&hsh=4&fclid=061f06bb-ee54-6f2c-2bf5-137eef2b6e19&psq=news+today&u=a1aHR0cHM6Ly90aW1lc29maW5kaWEuaW5kaWF0aW1lcy5jb20vaG9tZS9oZWFkbGluZXM&ntb=1")   
 
 elif "search in youtube" in query:
    speak("ooooooook")
    query=viceinput().lower()
    qry=query.replace(" ","+")
    webbrowser.open(f"https://www.youtube.com/results?search_query={qry} ")
 elif "search in google" in query:
    speak("ok ok ok ok")
    query=viceinput().lower()
    qry=query.replace(" ","+")
    webbrowser.open(f"https://www.google.com/search?q={qry}&sca_esv=1543b9c3e9f38e65&sxsrf=AE3TifOe4OM4kdlwS7Xx57A4qfUUDZmZkg%3A1748763731944&ei=UwQ8aMe1OKyq4-EPpNGKkQo&ved=0ahUKEwiHq6bI3M-NAxUs1TgGHaSoIqIQ4dUDCBA&oq={qry}&gs_lp=Egxnd3Mtd2l6LXNlcnAiDHl5eXl5IGFhYSBkeTIHECEYoAEYCjIHECEYoAEYCkjLN1CTBVijJHABeAGQAQCYAb0DoAGSEKoBCTAuMS40LjAuMrgBDMgBAPgBAZgCB6ACpQ_CAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICExAuGIAEGLADGEMYyAMYigXYAQHCAgUQIRifBcICCBAAGAoYDRgewgIGEAAYDRgewgIIEAAYCBgNGB7CAgsQABiABBiGAxiKBcICBRAAGO8FwgIGEAAYFhgewgIIEAAYFhgKGB7CAggQABiABBiiBJgDAIgGAZAGFLoGBggBEAEYCJIHCTEuMC4zLjEuMqAHmCayBwcyLTMuMS4yuAf7DsIHBzItMS41LjHIB20&sclient=gws-wiz-serp ")     
 elif "open chat gpt" in query:
    webbrowser.open("https://chat.openai.com/")  
