import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


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
        # print(e)
        print("Can't comprehend what you are saying. Can you say it again please....\n")
        speak("Can't comprehend what you are saying. Can you say it again please....")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zoheb.412010.cs@mhssce.ac.in', 'artificiallearning&machineintelligence')
    server.sendmail('zoheb.412010.cs@mhssce.ac.in', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # print("Press 'K' for input via keyboard\n \t\tor\nPress 'M' for input via microphone\n")
        # speak("Press 'K' for input via keyboard\n \t\tor\nPress 'M' for input via microphone")
        option = str(input())
        if option == 'M' or option == 'm':
            query = takeCommand().lower()
        elif option == 'K' or option == 'k':
            query = input("Type your query:\n")
        else:
            print("Enter valid input: ")

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:

            if 'brave browser' in query:
                url = "youtube.com" 
                path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
                webbrowser.get(path).open(url)

            elif 'mozilla browser' or 'firefox browser' or 'mozilla firefox' in query:
                url = "youtube.com" 
                path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
                webbrowser.get(path).open(url)

            else:
                url = "youtube.com"
                path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(path).open(url)

        elif 'google' in query:

            if 'brave browser' in query:
                url = "youtube.com" 
                path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
                webbrowser.get(path).open(url)

            elif 'mozilla browser' or 'firefox browser' or 'mozilla firefox' in query:
                url = "youtube.com" 
                path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
                webbrowser.get(path).open(url)
            
            else:
                url = "google.com"
                path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(path).open(url)

        elif 'stackoverflow' in query:

            if 'brave browser' in query:
                url = "youtube.com" 
                path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
                webbrowser.get(path).open(url)

            elif 'mozilla browser' or 'firefox browser' or 'mozilla firefox' in query:
                url = "youtube.com" 
                path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
                webbrowser.get(path).open(url)

            else:
                url = "stackoverflow.com"
                path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
                webbrowser.get(path).open(url)

        elif 'play music' in query:
            music_dir = 'D:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            # add to play specific music


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open music' in query:
            codePath = "D:\\Music"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "zoheb.412010.cs@mhssce.ac.in"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Zoheb. I am not able to send this email")

        elif 'quit' in query:
            break