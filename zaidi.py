from wikipedia.exceptions import DisambiguationError, PageError
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia
import sys
import webbrowser
import os
import smtplib


# Configure stdout for UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

# Initialize Text-to-Speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """Speak out the provided text."""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """Greets the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Assalamualaikum! I am Raodi Sir. Please tell me how may I help you.")


def takeCommand():
    """
    Listens to the microphone and returns the spoken query as a string.
    """
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
    """
    Sends an email using SMTP.
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Replace with your actual email credentials
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email.")


def search_wikipedia(query):
    """
    Searches Wikipedia for the given query and handles ambiguities or errors.
    """
    try:
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    except DisambiguationError as e:
        speak("Your search term is ambiguous. Here are some suggestions.")
        print(f"Ambiguous term: {query}. Suggestions:")
        for option in e.options[:5]:  # Limit to 5 suggestions
            print(f"- {option}")
            speak(option)
    except PageError:
        speak("Sorry, I could not find a page for your query.")
        print(f"No page found for: {query}")
    except Exception as e:
        speak("An error occurred while searching Wikipedia.")
        print(e)


def open_and_close_tab():
    """
    Opens a new browser tab, performs a task, and closes the tab.
    """
    try:
        driver = webdriver.Chrome(executable_path='path_to_driver')  # Update driver path
        driver.get("https://www.google.com")
        print("Tab opened: Google")
        time.sleep(5)  # Simulate some work
        driver.close()
        print("Tab closed")
    except Exception as e:
        print("Error with Selenium WebDriver:", e)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Task execution logic
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            search_query = query.replace("wikipedia", "").strip()
            search_wikipedia(search_query)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'  # Update path
            try:
                songs = os.listdir(music_dir)
                if songs:
                    os.startfile(os.path.join(music_dir, songs[0]))
                else:
                    speak("No songs found in the directory.")
            except FileNotFoundError:
                speak("Music directory not found.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Zaidis\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # Update path
            try:
                os.startfile(codePath)
            except FileNotFoundError:
                speak("VS Code not found at the specified path.")

        elif 'email to zaid' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "zaid@example.com"  # Replace with the recipient's email
                sendEmail(to, content)
            except Exception as e:
                print(e)
                speak("Sorry, I could not send the email.")
