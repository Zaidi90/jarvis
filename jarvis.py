import datetime
import pyttsx3
import speech_recognition
import requests
import os
from  bs4 import BeautifulSoup
import pyautogui
import random
import webbrowser



engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()
            
            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break
                
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank" in query:
                    speak("you are welcome, sir")
                    
                    
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                       kwebbrowser.open("https://www.youtube.com/results?search_query=safar+song")
                
                
                
                
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                     pyautogui.press("m")
                     speak("video muted")
                     
                elif "volume up" in query:
                     from keyboard import volumeup
                     speak("Turning volume up,sir")
                     volumeup()
                    
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                    
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                     from Dictapp import closeappweb
                     closeappweb(query)
                                  
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query) 
                    
                     
                elif "temperature" in query:
                   search = "temperature in karachi"
                   url = f"https://www.google.com/search?q={search}"
                   r  = requests.get(url)
                   data = BeautifulSoup(r.text,"html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"current{search} is {temp}")
                elif "weather" in query:
                   search = "temperature in karachi"
                   url = f"https://www.google.com/search?q={search}"
                   r  = requests.get(url)
                   data = BeautifulSoup(r.text,"html.parser")
                   temp = data.find("div", class_ = "BNeawe").text
                   speak(f"current{search} is {temp}")
                   
                
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                   
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")
                    
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to" + remember.read())

                      
    


    
                     

