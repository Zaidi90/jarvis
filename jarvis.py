from wikipedia.exceptions import DisambiguationError
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia 
import sys
import webbrowser
import os
import smtplib
# import selenium    

import time

# Change the default encoding to 'utf-8'
sys.stdout.reconfigure(encoding='utf-8')

query = "your search term here"  # Replace with the actual query

try:
    results = wikipedia.summary(query, sentences=2)
    print(results)
except DisambiguationError as e:
    print(f"Your search term '{query}' is ambiguous. It may refer to:")
    for option in e.options:
        print(f"- {option}")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime).datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Assalamualikum I am Raodi Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
           webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Zaidis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Zaid' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "Zaid yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Zaid bhai. I am not able to send this email");
                
#  def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
#     def wishMe():
                
    
# def open_and_close_tab():
#     # Initialize the WebDriver (Replace 'path_to_driver' with your WebDriver's path)
#    webbrowser = webbrowser.Chrome(executable_path='path_to_browser')
    
#     # Open a new tab
#  webbrowser.open("Open a new tab")
# print()
#     # Wait for a few seconds to simulate work
# time.sleep(5)
    
# webbrowser.close()
# print("Tab closed")

# if __name__ == "__main__":
#     open_and_close_tab()
#     # Close the tab
    
   



        
       