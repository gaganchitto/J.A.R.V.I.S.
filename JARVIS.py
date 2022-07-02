import pyttsx3  # windows ki cheeze use krne k liy
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser  # web browse krke n liy module
import os  # helps in play music
import smtplib
import googlesearch
import requests
import json
from selenium import webdriver
from time import sleep

engine = pyttsx3.init('sapi5')  # window ki inbuild voice use krenge
voices = engine.getProperty('voices')
# print(voices[1].id) voices[0].id ye apne pc ki voice batate h
newrate = 190
engine.setProperty('voice', voices[1].id)  # hamne girl ki voice choose ki
engine.setProperty('rate', newrate)


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YourMail', 'YourMailPassword')
    server.sendmail('YourMail', to, content)
    server.close()


def speak(audio):  # jarvis ko awaaz denge
    engine.say(audio)
    engine.runAndWait()


def pranamKro():
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        speak("Good Morning sir")
    elif hr >= 12 and hr < 18:
        speak("Good Afternoon sir")
    else:
        speak("Good Evening sir")
    speak("I'm Jarvis PLease tell how may i help you .")


def search():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold =300
        r.non_speaking_duration = 0.5
        r.pause_threshold = 1
        # r.adjust_for_ambient_noise(source, duration=1)
        # r.energy_threshold=100
        # r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source, timeout=10, phrase_time_limit=3)
    try:
        print("Recognizing....")
        string = r.recognize_google(audio, language='en-in')
        print(f"You said: {string.lower()}\n")
        if 'nothing' in string:
            speak("Thanks for using my service have a good day.")
        else:
            a = string.split(" ")
            l = len(a)
            if l == 1:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}")
            elif l == 2:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}")
            elif l == 3:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}")
            elif l == 4:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}")
            elif l == 5:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}")
            elif l == 6:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}")
            elif l == 7:
                speak("Here are the results")
                webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}")
    except Exception as e:
        print(e)
        print("Say that again...")
        speak("Please speak a bit louder")
        search()
        return "None"
    return string


def Intellisense(string):
    try:
        a = string.split(" ")
        l = len(a)
        if l == 1:
            speak("Here are the results")
            webbrowser.open(f"https://www.google.com/search?q={a[0]}")
        elif l == 2:
            speak("Here are the results")
            webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}")
        elif l == 3:
            (speak("Here are the results"))
            webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}")
        elif l == 4:
            speak("Here are the results")
            webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}")
        elif l == 5:
            speak("Here are the results")
            webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}")
        elif l == 6:
            speak("Here are the results")
            webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}")
        elif l == 7:
            speak("Here are the results")
            webbrowser.open(f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}")
        elif l == 8:
            speak("Here are the results")
            webbrowser.open(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}+{a[7]}")
        elif l == 9:
            speak("Here are the results")
            webbrowser.open(
                f"https://www.google.com/search?q={a[0]}+{a[1]}+{a[2]}+{a[3]}+{a[4]}+{a[5]}+{a[6]}+{a[7]}+{a[8]}")
    except Exception as e:
        print(e)
        results = wikipedia.summary(string, sentences=2)
        print(results)
        speak(results)


def takeMyOrder():
    # ab ham order denge (mic s input leke output m string denge)
    order = sr.Recognizer()
    with sr.Microphone() as source:  # ham microophone k command as sourcele rhe h
        print("Listening...")  # user ko bataynge ki ha ye kaam kr rha h microphone
        # order.energy_threshold=300
        order.adjust_for_ambient_noise(source, duration=1)
        order.non_speaking_duration = 0.4
        order.pause_threshold = 0.40001  # agr word k baad sec kuch ni bola toh aage badd jayga
        audio = order.listen(source)

        # ab ham dekhege ye kaam kr rha h ya nhi
        try:
            print("Recognizing....")
            query = order.recognize_google(audio, language='en-in')
            print(f"You said - {query}\n")

        except Exception as e:
            # print(e)

            print("Say that again please...")
            return "None"
        return query


if __name__ == '__main__':
    pranamKro()
    while True:
        query = takeMyOrder()
        query = query.lower()
        # logic

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")  # hamne jo bola usme s wikipedia hata dega
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak("Here you go to Google")
            print("Here you go to Google")
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
            speak("What do you want to search")
            search()

        elif 'open stack overflow' in query:
            speak("Opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'wish mam' in query:
            speak(
                "Good Afternoon Mam, this is Jarvis made by Akshat and Gagan. I can do the following work for you : first, I can send a mail on beahalf of you. second, I can play music and entertain you. third, I can do any google search for you. Tell me mam how may i help you ?")

        elif 'play music' in query:
            music = "D:\\Music"
            songs = os.listdir(music)  # iss directry k saare song ki list bana dega
            # print(songs)
            os.startfile(os.path.join(music, songs[0]))

        elif 'open brave' in query:
            path = "C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(path)

        elif "today's news headlines" in query:
            speak("serching news..")
            try:
                jsonObj = requests.get(
                    "http://newsapi.org/v2/top-headlines?country=in&apiKey=685fe1bef34f463a8469ac2dbb7f78c7")
                data = json.loads(jsonObj.text)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in range(0, 4):
                    print(str(i) + '.' + data['articles'][item]['title'] + "\n")
                    print(data['articles'][item]['description'])
                    speak(data['articles'][item]['description'])
                    i += 1
            except Exception as e:
                print(str(e))

        elif "email to kumar" in query:
            try:
                speak("What should I say?")
                content = takeMyOrder()
                to = "2019kucp1004@iiitkota.ac.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry not able to send email right now!")


        elif "email to me" in query:
            try:
                speak("What should I say?")
                content = takeMyOrder()
                to = "2019kucp1002@iiitkota.ac.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry not able to send email right now!")


        elif "email to akshat" in query:
            try:
                speak("What should I say?")
                content = takeMyOrder()
                to = "2019kucp1022@iiitkota.ac.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry not able to send email right now!")

        elif "email to digvijay" in query:
            try:
                speak("What should I say?")
                content = takeMyOrder()
                to = "palsinghdigvijay@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry not able to send email right now!")

        elif 'search' in query:
            Intellisense(query)

        elif 'login to instagram' in query:
            speak("here you go to instagram")
            driver = webdriver.Chrome('chromedriver.exe')
            driver.get('http://www.instagram.com/')
            driver.maximize_window()
            sleep(3)

            username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            username.send_keys('InstaUserName')
            password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            password.send_keys('InstaPAssword')
            sleep(1)
            login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
            login.click()
