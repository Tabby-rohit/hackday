import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import sounddevice as sd
import numpy as np
import json
from google import genai
os.environ["GEMINI_API_KEY"] = "AIzaSyBJfEYNEZyupwXAJ4ASA2EjE3L9CqivaNk"
client = genai.Client()


eng=pyttsx3.init("sapi5")
vic=eng.getProperty("voices")
eng.setProperty("voice",vic[1].id)
# print(vic[1].id)
def speak(aud):
    eng = pyttsx3.init()
    eng.say(aud)
    eng.runAndWait()
    eng.stop()
def wish():
    hr=int(datetime.datetime.now().hour)
    if hr>0 and hr<12:
        speak("good morning sir how are you")
    elif hr>12 and hr<18:
        speak("good afternoon")
    elif hr>18 and hr<20:
        speak("good evening")    
    speak("I am yor personal assistant jarvis how may i help you") 


def get_today_tasks():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open("tasks.json", "r") as file:
        data = json.load(file)
    
    return data.get(today, [])


def viceinput():
    r = sr.Recognizer()
    
    fs = 15000
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
todos=get_today_tasks()
wish()
a=True
while a==True:
 query=viceinput().lower()
 if "wikipedia" in query :
    query=query.replace("wikipedia","")
    speak(f"according to wikipedia{wikipedia.summary(query,sentences=2)}")
 elif "open youtube" in query:
    speak("opening youtube") 
    webbrowser.open("youtube.com") 
    
 elif "close" in query:
    a=False   
 elif "open google" in query:
    webbrowser.open("google.com")
 elif "news" in query:
    webbrowser.open("https://www.bing.com/ck/a?!&&p=e7464a70a9e2ce997e7b8b1d2b00eea4d2f4faf30f60f3e1b23212063d7425f7JmltdHM9MTc0ODY0OTYwMA&ptn=3&ver=2&hsh=4&fclid=061f06bb-ee54-6f2c-2bf5-137eef2b6e19&psq=news+today&u=a1aHR0cHM6Ly90aW1lc29maW5kaWEuaW5kaWF0aW1lcy5jb20vaG9tZS9oZWFkbGluZXM&ntb=1")   
 
 elif "search in youtube" in query:
    
    query=viceinput().lower()
    qry=query.replace(" ","+")
    webbrowser.open(f"https://www.youtube.com/results?search_query={qry} ")
 elif "search in google" in query:
    
    query=viceinput().lower()
    qry=query.replace(" ","+")
    webbrowser.open(f"https://www.google.com/search?q={qry}&sca_esv=1543b9c3e9f38e65&sxsrf=AE3TifOe4OM4kdlwS7Xx57A4qfUUDZmZkg%3A1748763731944&ei=UwQ8aMe1OKyq4-EPpNGKkQo&ved=0ahUKEwiHq6bI3M-NAxUs1TgGHaSoIqIQ4dUDCBA&oq={qry}&gs_lp=Egxnd3Mtd2l6LXNlcnAiDHl5eXl5IGFhYSBkeTIHECEYoAEYCjIHECEYoAEYCkjLN1CTBVijJHABeAGQAQCYAb0DoAGSEKoBCTAuMS40LjAuMrgBDMgBAPgBAZgCB6ACpQ_CAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICExAuGIAEGLADGEMYyAMYigXYAQHCAgUQIRifBcICCBAAGAoYDRgewgIGEAAYDRgewgIIEAAYCBgNGB7CAgsQABiABBiGAxiKBcICBRAAGO8FwgIGEAAYFhgewgIIEAAYFhgKGB7CAggQABiABBiiBJgDAIgGAZAGFLoGBggBEAEYCJIHCTEuMC4zLjEuMqAHmCayBwcyLTMuMS4yuAf7DsIHBzItMS41LjHIB20&sclient=gws-wiz-serp ")     
 elif "open chat gpt" in query:
    webbrowser.open("https://chat.openai.com/")
 elif "play music" in query:
    webbrowser.open("https://music.youtube.com/") 
 elif "open code" in query:
    codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)
 elif "open command prompt" in query:
    os.system("start cmd")
 elif "open whatsapp" in query:
    webbrowser.open("https://web.whatsapp.com/")       
 elif "open instagram" in query:
    webbrowser.open("https://www.instagram.com/")
 elif "open gmail" in query:
      webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
 elif "open drive" in query:     
    webbrowser.open("https://drive.google.com/drive/my-drive")
 elif "shut down pc" in query:
    os.system("shutdown /s /t 5")
    print("shutting down in 5 seconds")
 elif "restart pc" in query:
    os.system("shutdown /r /t 5")
    print("restarting in 5 seconds")
 elif "sleep pc" in query:
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    print("sleeping in 5 seconds")
 elif "hibernate pc" in query:
    os.system("rundll32.exe powrprof.dll,SetSuspendState Hibernate")
    print("hibernating in 5 seconds")
 elif "open notepad" in query:
    os.system("start notepad")
 elif "what are today's task" in query:
    if todos:
        speak("your tasks for today are:")
        for task in todos:
            speak(task)
            print(task)
    else:
        speak("you have no tasks for today")
 elif "add task" in query:
    speak("what task do you want to add")
    task=viceinput().lower()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open("tasks.json", "r") as file:
        data = json.load(file)
    
    if today in data:
        data[today].append(task)
    else:
        data[today] = [task]
    
    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)
    
    speak("task added successfully")
 elif "remove task" in query:
    speak("which task do you want to remove")
    task=viceinput().lower()
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    with open("tasks.json", "r") as file:
        data = json.load(file)
    
    if today in data and task in data[today]:
        data[today].remove(task)
        with open("tasks.json", "w") as file:
            json.dump(data, file, indent=4)
        speak("task removed successfully")
    else:
        speak("task not found")
 elif "who are you" in query or "hu r u" in query:
    speak("I am jarvis your personal assistant created by Rohit")     
 elif"jarvis what":
    
    query=query.replace("jarvis what","what")    
    response = client.models.generate_content(
   model="gemini-3-flash-preview", contents=query
    )
    print(response.text)
    speak(response.text.replace("#","").replace("*","")) 
            
