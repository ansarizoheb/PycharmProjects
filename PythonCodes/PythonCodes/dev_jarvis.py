import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes
import pyautogui
from plyer import notification
from bs4 import BeautifulSoup
import requests
import smtplib

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak_va("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak_va("Good Afternoon!")

    else:
        speak_va("Good Evening!")

    speak_va("I am Jarvis Sir. Please tell me how may I help you")

def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('recognition is on....')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print('this is the query that was made....', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)

def input_query_keyboard():
    query = input("Please type your query: ")
    return query

def report_time():
    current_time = datetime.datetime.now().strftime('%I:%M %p')
    return current_time


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('zoheb.412010.cs@mhssce.ac.in', 'artificiallearning&machineintelligence')
    server.sendmail('zoheb.412010.cs@mhssce.ac.in', to, content)
    server.close()

def make_request(url):
  response = requests.get(url)
  return response.text

def activate_va():
    print('''Press M for query via Microphone
            or
Press K for query via keyboard''')
    wishMe()
    choice = str(input())
    if choice == 'K' or choice == 'k':
        user_query = input_query_keyboard()
    elif choice == 'M' or choice == 'm':
        user_query = input_query()
    print('user query ....', user_query)
    if 'time' in user_query:
        current_time = report_time()
        print(f"the current time is {current_time}")
        speak_va(f"the current time is {current_time}")
    elif 'youtube' in user_query:

        if 'brave' in user_query:
            url = "https://www.youtube.com/" 
            path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            webbrowser.get(path).open(url)

        elif 'mozilla' or 'firefox' in user_query:
            url = "https://www.youtube.com/" 
            path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(path).open(url)

        if 'chrome' in user_query:
            url = "https://www.youtube.com/"
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.ex  %s'
            webbrowser.get(path).open(url)

        else:
            url = "https://www.youtube.com/"
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.ex  %s'
            webbrowser.get(path).open(url)

    elif 'google' in user_query:

        if 'brave' in user_query:
            url = "https://www.google.com/" 
            path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            webbrowser.get(path).open(url)

        elif 'mozilla' or 'firefox' in user_query:
            url = "https://www.google.com/" 
            path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(path).open(url)

        if 'chrome' in user_query:
            url = "https://www.google.com/"
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(path).open(url)

        else:
            url = "https://www.google.com/"
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(path).open(url)

    elif 'stackoverflow' in user_query:

        if 'brave' in user_query:
            url = "https://stackoverflow.com/" 
            path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s'
            webbrowser.get(path).open(url)

        elif 'mozilla' or 'firefox' in user_query:
            url = "https://stackoverflow.com/" 
            path = 'C:/Program Files/Mozilla Firefox/firefox.exe %s'
            webbrowser.get(path).open(url)

        elif 'chrome' in user_query:
            url = "https://stackoverflow.com/"
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(path).open(url)
        
        else:
            url = "https://stackoverflow.com/"
            path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(path).open(url)

    elif 'open website' in user_query:
        speak_va(
            "Please type the name of the website that you want to open (specify the full url) \n")
        website_name = input()
        print(website_name)
        webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(website_name)
        speak_va(f"{website_name} opened.")

    elif 'wikipedia' in user_query:
        speak_va("Searching on Wikipedia")
        user_query = user_query.replace('wikipedia', ' ')
        result = wikipedia.summary(user_query, sentences=4)
        print(result)
        speak_va(result)

    elif 'joke' in user_query:
        random_joke = pyjokes.get_joke()
        print(random_joke)
        speak_va(random_joke)

    elif 'screenshot' in user_query:
        image = pyautogui.screenshot()
        image.save('screenshot.png')
        speak_va('Screenshot taken.')

    elif 'search' in user_query:
        if 'brave' in user_query:
            speak_va("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.brave.com/search?q={search_term}"
            webbrowser.get(
                'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(search_url)
            speak_va(f"here are the results for the search term: {search_term}")
        elif 'firefox' in user_query:
            speak_va("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.firefox.com/search?q={search_term}"
            webbrowser.get(
                'C:/Program Files/Mozilla Firefox/firefox.exe %s').open(search_url)
            speak_va(f"here are the results for the search term: {search_term}")
        else:
            speak_va("What do you want me to search for (please type) ? ")
            search_term = input()
            search_url = f"https://www.google.com/search?q={search_term}"
            webbrowser.get(
                'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe %s').open(search_url)
            speak_va(f"here are the results for the search term: {search_term}")
    
    elif 'send email' in user_query:
            try:
                speak_va("What should I say?")
                content = input_query()
                to = input("Enter the recipient email id.")
                sendEmail(to, content)
                print("Email has been sent!")
                speak_va("Email has been sent!")
            except Exception as e:
                print(e)
                speak_va("Sorry my friend Zoheb. I am not able to send this email")

    elif 'covid stats' in user_query:
      html_data = make_request('https://www.worldometers.info/coronavirus/')
      # print(html_data)
      soup = BeautifulSoup(html_data, 'html.parser')
      total_global_row = soup.find_all('tr', {'class': 'total_row'})[-1]
      total_cases = total_global_row.find_all('td')[2].get_text()
      new_cases = total_global_row.find_all('td')[3].get_text()
      total_recovered = total_global_row.find_all('td')[6].get_text()
      print('total cases : ', total_cases)
      print('new cases', new_cases[1:])
      print('total recovered', total_recovered)
      notification_message = f" Total cases : {total_cases}\n New cases : {new_cases[1:]}\n Total Recovered : {total_recovered}\n"
      notification.notify(
        title="COVID-19 Statistics",
        message=notification_message,
        timeout=5
      )
      speak_va("here are the stats for COVID-19")

    elif 'quit' or 'exit' in user_query:
        return None
        
while True:
    activate_va()