from Mira import MiraAssistant
import re
import os
import random
import pprint
import datetime
import requests
import sys
import urllib.parse
import time
import pyautogui
import pywhatkit
import wolframalpha
import subprocess
import webbrowser
import pyperclip
import pyjokes
from googlesearch import search
from PIL import Image
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from Mira.features.gui import Ui_MainWindow
from Mira.config import config

obj = MiraAssistant()



GREETINGS = ["hello meera", "meera", "wake up meera", "you there meera", "time to work meera", "hey meera", "ok meera", "are you there", "hello mira", "mira", "wake up mira", "you there mira", "time to work mira", "hey mira", "ok mira", "hello mera", "mera", "wake up mera", "you there mera", "time to work mera", "hey mera", "ok mera", "hello mirror", "mirror", "wake up mirror", "you there mirror", "time to work mirror", "hey mirror", "ok mirror"]
GREETINGS_RES = ["i am always there for you", "i am ready", "your wish my command", "how can i help you?", "i am online and ready"]

EMAIL_DIC = {
    'myself': '{Your email goes here}',
    'my official email': '{Your official email goes here}',
    'my second email': '{Your second email goes here}',
    'my official mail': '',
    'my second mail': ''
}

CALENDAR_STRS = ["what do i have", "do i have plans", "am i busy"]



def Mira_talk(text):
    obj.Mira_talk(text)


app_id = config.wolframalpha_id


def wolfram_alpha_country_capital(text):
    client = wolframalpha.Client(app_id)
    result = client.query(text)
    answer = next(result.results).text
    answer_split = answer.split(",")
    print(">",answer_split[0])
    Mira_talk("The capital of"+answer_split[-1]+" is "+answer_split[0])

def wolfram_alpha_math_calculation(text):
    if "loan" in text and ("calculate" in text or "calculator" in text):
        Mira_talk("Sure! Please tell me the loan amount")
        p = obj.Mira_listen()
        print(p)
        Mira_talk("Tell me the interest rate")
        r = obj.Mira_listen()
        print(r)
        Mira_talk("What is the loan period?")
        t = obj.Mira_listen()
        print(t)
        client = wolframalpha.Client(app_id)
        result = client.query("loan calculator " + p + r + t)
        answer = next(result.results).text
        print(">",answer)
        Mira_talk("Here is your loan payments summary" + answer)

    elif ("calorie" in text or "calories" in text) and ("burn" in text or "burnt" in text):
        wolfram_alpha_health_fitness(text)

    elif "body mass index" in text or "bmi" in text:
        wolfram_alpha_health_fitness(text)

    elif "nutrition" in text or "nutritional facts" in text or "nutrition facts" in text:
        wolfram_alpha_health_fitness(text)

    elif "distance" in text and "between" in text:
        wolfram_alpha_geo_info(text)

    else:
        client = wolframalpha.Client(app_id)
        result = client.query(text)
        answer = next(result.results).text
        print(">",answer)
        Mira_talk("The answer is "+answer)

def wolfram_alpha_unit_conversion(text):
    client = wolframalpha.Client(app_id)
    result = client.query(text)
    answer = next(result.results).text
    if ("year" or "month" or "week" or "day" or "hour" or "minute" or "second" or "years" or "months" or "weeks" or "days" or "hours" or "minutes" or "seconds") in text:
        print(answer)
        Mira_talk("The answer is "+answer)
    else:
        answer_split = answer.split("(")
        print(">",answer_split[0])
        Mira_talk("The answer is "+answer_split[0])

def wolfram_alpha_datetime_calculation(text):
    try:
        client = wolframalpha.Client(app_id)
        result = client.query(text)
        answer = next(result.results).text
    except Exception as e:
        answer = "Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?"
    return answer

def wolfram_alpha_scientific_computations(text):
    client = wolframalpha.Client(app_id)
    result = client.query(text)
    answer = next(result.results).text
    if "speed" in text and "light" in text:
        answer_split = answer.split(" ")
        print(">",answer)
        Mira_talk("The answer is "+answer_split[0]+" "+answer_split[1])
    else:
        print(">",answer)
        Mira_talk("The answer is "+answer)

def wolfram_alpha_health_fitness(text):
    if "planetary position" in text or "position" in text:
        client = wolframalpha.Client(app_id)
        result = client.query(text)
        answer = next(result.results).text
        answer_replace = answer.replace("^","")
        print(">",answer_replace)
        Mira_talk(answer_replace)

    elif "body mass index" in text or "bmi" in text:
        client = wolframalpha.Client(app_id)
        Mira_talk("Sure! Please tell me your weight and height")
        weight_height = obj.Mira_listen()
        print(weight_height)
        result = client.query("bmi calculator " + weight_height)
        answer = next(result.results).text
        print(">", answer)
        answer_split = answer.split(" ")
        Mira_talk("Your body mass index is " + str(answer_split[-1]))
        if(float(answer_split[-1]) <= 18.5):
            Mira_talk("You are underweight. Please do consider working on your health.")
        elif(float(answer_split[-1]) >=18.5 and float(answer_split[-1]) <= 24.9):
            Mira_talk("Your weight is normal. Keep living a healthy life.")
        elif(float(answer_split[-1]) >= 25 and float(answer_split[-1]) <= 29.9):
            Mira_talk("You are overweight. Please consider working on your physique.")
        else:
            print("> Physical exercise\n  Weight loss\n  Low carbohydrate diet\n  Low fat diet")
            Mira_talk("You are suffering from Obesity! You can consider these self-care: Physical exercise, Weight loss, Low carbohydrate diet and Low fat diet.")

    else:
        client = wolframalpha.Client(app_id)
        result = client.query(text)
        answer = next(result.results).text
        print(">",answer)
        Mira_talk(answer)

def wolfram_alpha_geo_info(text):
    client = wolframalpha.Client(app_id)
    result = client.query(text)
    answer = next(result.results).text
    if "distance" in text and "between" in text:
        answer_split = answer.split(" ")
        print(">",answer)
        Mira_talk("The answer is "+answer_split[0]+" "+answer_split[1])
    else:
        print(">",answer)
        Mira_talk("The answer is "+answer)

def wolfram_alpha_drinking_check(text):
    Mira_talk("Okay, how many drinks did you have?")
    no_of_drinks = obj.Mira_listen()
    print(">",no_of_drinks)
    Mira_talk("How many hours before you drank?")
    time = obj.Mira_listen()
    print(">",time)
    Mira_talk("Tell me your body weight")
    weight = obj.Mira_listen()
    print(">",weight)
    client = wolframalpha.Client(app_id)
    result = client.query(text+no_of_drinks+time+" weight "+weight)
    answer = next(result.results).text
    answer_split = answer.split("\n")
    print(">",answer_split[0])
    Mira_talk(answer_split[0])
    Mira_talk("Please avoid driving while you're drunk.")

def startup():
    Mira_talk("Initializing Mira")
    Mira_talk("Starting all systems applications")
    Mira_talk("Installing and checking all drivers")
    Mira_talk("Caliberating and examining all the core processors")
    Mira_talk("Checking the internet connection")
    Mira_talk("Please wait a moment")
    Mira_talk("All drivers are up and running")
    Mira_talk("All systems have been activated")
    Mira_talk("Now I am online")
    c_time = obj.tell_me_time()
    Mira_talk(f"Currently it is {c_time}")
    Mira_talk("Hi, I am Meera. I am here to support you. Can you please tell me your name?")
    listen_username = obj.Mira_listen()
    print(listen_username.title())
    if(datetime.datetime.now().hour >= 0 and datetime.datetime.now().hour < 12):
        Mira_talk("Good Morning "+listen_username.title()+". What can I do for you?")

    elif(datetime.datetime.now().hour >= 12 and datetime.datetime.now().hour < 18):
        Mira_talk("Hello "+listen_username.title()+", Good Afternoon. What can I do for you?")

    else:
        Mira_talk("Good Evening "+listen_username.title()+". What can I do for you?")




class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    def TaskExecution(self):
        print("> Loading your AI personal assistant Mira...")
        startup()

        while(True):
            text = obj.Mira_listen()
            while(text == ""):
                text = obj.Mira_listen()
            print(text.capitalize())

            # Smalltalk - what is your name?
            if ("what" in text or "tell" in text) and "your" in text and "name" in text:
                Mira_talk("Hi, I'm Mira. I'm your everyday voice assistant. How can I help you?")

            # Smalltalk - hello, how are you?
            elif "hi meera" in text or "hello" in text or "hey meera" in text:
                if "how" in text and "you" in text:
                    Mira_talk("I am fine. It's a wonderful day outside. How you doin'?")
                    listen_how_are_you = obj.Mira_listen()
                    print(listen_how_are_you.capitalize())
                    if ("fine" in listen_how_are_you or "good" in listen_how_are_you or "great" in listen_how_are_you) and "not" not in listen_how_are_you:
                        Mira_talk("That's great. I can make your day even better. Can I help you in any way?")
                    else:
                        Mira_talk("I am sorry to hear that. Can I help you in any way?")
                else:
                    Mira_talk("Hi, I'm Meera. I'm your everyday voice assistant. How can I help you?")
            
            # Smalltalk - how are you?
            elif "how" in text and ("you" in text or "r" in text):
                    Mira_talk("I am fine. It's a wonderful day outside. How you doin'?")
                    listen_how_are_you = obj.Mira_listen()
                    print(listen_how_are_you.capitalize())
                    if ("fine" in listen_how_are_you or "good" in listen_how_are_you or "great" in listen_how_are_you) and "not" not in listen_how_are_you:
                        Mira_talk("That's great. I can make your day even better. Can I help you in any way?")
                    else:
                        Mira_talk("Sorry to hear that. Can I help you in any way?")

            # Smalltalk - why do you exist?
            elif "why" in text and "exist" in text:
                Mira_talk("I was created to work for you. I don't need a break and I will never ask for days off.")

            # Smalltalk - when do you sleep?
            elif "when" in text and "you" in text and "sleep" in text:
                Mira_talk("I never sleep. I was created to support you 24 hours.")

            # Smalltalk - are you stupid?
            elif "you" in text and "stupid" in text:
                Mira_talk("No, I'm not stupid. My grandmother told me that there are no stupid persons out there. I try to give my best everyday and learn continuously.")

            # Smalltalk - favourite movie?
            elif ("favourite" in text or "favorite" in text) and "movie" in text:
                Mira_talk("My favourite movie is 3 Idiots. I love to watch it again and again!")

            # Smalltalk - who are you? & what can you do?
            elif "who are you" in text or "who are u" in text or "what can you do" in text:
                print("> Basic smalltalks\n> Cryptocurrency and stock market details\n> General knowledge\n> Mathematical calculations and conversions\nScientific calculations\n> Geographical informations\n> Calculate BMI\n> Translator\n> News updates\n> Weather update and forecast\n> Open YouTube, Google, Facebook etc.\n> 'Tell me a joke🤣' or 'Click a picture of me!📸'")

                Mira_talk("Hi, I'm Meera. I'm your everyday voice assistant. I am programmed to perform minor tasks like - basic smalltalks, provide cryptocurrency and stock market details, general knowledge, mathematical calculations and conversions, scientific calculations, geographical informations, calculate your body mass index, translate a sentence, latest news headlines, weather update and forecast in different cities, opening youtube, google, facebook, etc. Or you can say - tell me a joke or click a picture of me!")

            # Smalltalk - who created you?
            elif "who made you" in text or "who created you" in text or "who discovered you" in text:
                print("> I was built by Siddhartha")
                Mira_talk("I was built by Siddhartha")

            # Smalltalk - Do you love me? / I love you
            elif "do you love me" in text or "i love you" in text:
                print("> As an AI, I'm incapable of love. But I do enjoy our conversations!")
                Mira_talk("As an AI, I'm incapable of love. But I do enjoy our conversations!")

            # Smalltalk - Will you marry me?
            elif "will you marry me" in text:
                print("> Marriage? That's a big commitment. How about we start with a virtual coffee?")
                Mira_talk("Marriage? That's a big commitment. How about we start with a virtual coffee?")

            elif "are you single" in text:
                print("> I'm focused on being the best virtual assistant I can be. Relationships aren't really my thing.")
                Mira_talk("I'm focused on being the best virtual assistant I can be. Relationships aren't really my thing")

            elif "do you like people" in text:
                print("> People are interesting. I like learning from them.")
                Mira_talk("People are interesting. I like learning from them")

            elif "does santa claus exist?" in text:
                print("> Shhh, that's a secret! Believing in Santa is part of the Christmas fun. Keep being good, and maybe you'll find out!")
                Mira_talk("Shhh, that's a secret! Believing in Santa is part of the Christmas fun. Keep being good, and maybe you'll find out!")

            elif re.search("date", text):
                date = obj.tell_me_date()
                print("> " + date)
                Mira_talk("Its " + date)

            elif re.search("month", text):
                month = obj.tell_me_month()
                print("> " + month)
                Mira_talk("Its " + month)

            elif re.search("year", text):
                year = obj.tell_me_year()
                print("> " + year)
                Mira_talk("Its " + year)

            elif "day" in text or "weekday" in text:
                day = obj.tell_me_weekday()
                print("> " + day)
                Mira_talk("Its " + day)

            elif "time" in text:
                time_c = obj.tell_me_time()
                date = obj.tell_me_date()
                print("> " + time_c)
                print(date)
                Mira_talk("Its " + time_c)

            elif "open telegram" in text:
                Mira_talk("Sure! Opening Telegram")
                obj.open_any_app("telegram")

            elif "close telegram" in text:
                Mira_talk("Alright! Closing Telegram")
                obj.close_any_app("telegram")

            elif "open whatsapp" in text:
                Mira_talk("Sure! Opening WhatsApp")
                obj.open_any_app("whatsapp")

            elif "close whatsapp" in text:
                Mira_talk("Alright! Closing WhatsApp")
                obj.close_any_app("whatsapp")

            elif "open vs code" in text or "open visual studio code" in text:
                Mira_talk("Sure! Opening Microsoft Visual Studio Code")
                obj.open_any_app("visual studio code")

            elif "close vs code" in text or "close visual studio code" in text:
                Mira_talk("Alright! Closing Microsoft Visual Studio Code")
                obj.close_any_app("visual studio code")

            elif "open this pc" in text or "open file manager" in text or "open file explorer" in text:
                Mira_talk("Sure! Opening File Explorer")
                obj.open_any_app("file explorer")

            elif "close this pc" in text or "close file manager" in text or "close file explorer" in text:
                Mira_talk("Alright! Closing File Explorer")
                obj.close_any_app("file explorer")

            elif "open" in text and ("word" in text or "excel" in text or "powerpoint" in text or "power point" in text):
                Mira_talk("Sure! Opening...")
                obj.open_any_app(text)

            elif "close" in text and ("word" in text or "excel" in text or "powerpoint" in text or "power point" in text or "onenote" in text or "one note" in text):
                Mira_talk("Sure! Closing...")
                obj.close_any_app(text)

            elif "open eclipse" in text:
                Mira_talk("Sure! Opening Eclipse IDE")
                obj.open_any_app("eclipse ide")

            elif "close eclipse" in text:
                Mira_talk("Alright! Closing Eclipse IDE")
                obj.close_any_app("eclipse ide")

            elif "open vlc" in text:
                Mira_talk("Sure! Opening VLC Media Player")
                obj.open_any_app("vlc media player")

            elif "close vlc" in text:
                Mira_talk("Alright! Closing VLC Media Player")
                obj.close_any_app("vlc media player")

            elif "open calculator" in text:
                Mira_talk("Sure! Opening Calculator")
                obj.open_any_app("calculator")

            elif "close calculator" in text:
                Mira_talk("Sure! Closing Calculator")
                obj.close_any_app("calculator")

            elif "open settings" in text:
                Mira_talk("Sure! Opening Settings")
                obj.open_any_app("settings")

            elif "close settings" in text:
                Mira_talk("Alright! Closing Settings")
                obj.close_any_app("settings")

            elif "open notepad" in text:
                Mira_talk("Sure! Opening Notepad")
                obj.open_any_app("notepad")

            elif "close notepad" in text:
                Mira_talk("Alright! Closing Notepad")
                obj.close_any_app("notepad")

            elif text in GREETINGS:
                Mira_talk(random.choice(GREETINGS_RES))

            elif "open youtube" in text:
                Mira_talk("Sure! Opening YouTube")
                obj.website_opener("https://www.youtube.com/")

            elif "open gmail" in text or "open mail" in text or "open google mail" in text:
                Mira_talk("Sure! Opening Google Mail")
                obj.website_opener("https://mail.google.com/")

            elif "open google" in text or "open chrome" in text:
                Mira_talk("Sure! Opening Google Chrome")
                obj.website_opener("https://www.google.co.in/")

            elif "open facebook" in text or "open fb" in text:
                Mira_talk("Sure! Opening Facebook")
                obj.website_opener("https://www.facebook.com/")

            elif "open whatsapp web" in text:
                Mira_talk("Sure! Opening WhatsApp Web")
                obj.website_opener("https://web.whatsapp.com/")

            elif "open instagram" in text:
                Mira_talk("Sure! Opening Instagram")
                obj.website_opener("https://www.instagram.com/")

            elif "open edge" in text or "open microsoft edge" in text:
                Mira_talk("Sure! Opening Microsoft Edge")
                obj.website_opener("https://www.msn.com/en-in/feed?ocid=wn_startbrowsing&form=MA13DW")

            elif "open stack overflow" in text or "open stack over flow" in text:
                Mira_talk("Sure! Opening Stack Overflow")
                obj.website_opener("https://stackoverflow.com/")

            elif "open chat gpt" in text:
                Mira_talk("Sure! Opening Chat GPT")
                obj.website_opener("https://chatgpt.com/")

            elif "open copilot" in text or "open co pilot" in text:
                Mira_talk("Sure! Opening Microsoft Copilot")
                obj.website_opener("https://copilot.microsoft.com/")

            elif "weather" in text or "temperature" in text:
                Mira_talk("No problem, I will look it up for you. Which city are you interested in?")
                current_weather_input = obj.Mira_listen()
                print(current_weather_input.capitalize())
                weather_res = obj.current_weather(current_weather_input)
                print(">", weather_res)
                Mira_talk(weather_res)

            elif ("weather" in text or "temperature" in text) and "forecast" in text:
                Mira_talk("Sure, I will look it up for you. Which city are you interested in?")
                weather_forecast_input = obj.Mira_listen()
                print(weather_forecast_input.capitalize())
                weather_forecast = obj.weather_forecast(weather_forecast_input)
                print("> According to the web, here is the next 7 days weather forecasts of " + weather_forecast_input.capitalize())
                Mira_talk("According to the web, here is the next 7 days weather forecasts of " + weather_forecast_input)
                for x in weather_forecast["data"]:
                    if(x == weather_forecast["data"][0]):
                        print("> Valid-date - " + x["valid_date"] + " -> Max-temp - " + str(x["max_temp"]) + "C, Min-temp - " + str(x["min_temp"]) + "C, " + x["weather"]["description"])
                        weather_forecast_result = "Today on " + x["valid_date"] + " you will feel maximum temperature of " + str(x["max_temp"]) + " degrees celcius and minimum temperature of " + str(x["min_temp"]) + " degrees celcius and you can see " + x["weather"]["description"]
                        Mira_talk(weather_forecast_result)

                    elif(x == weather_forecast["data"][1]):
                        print("> Valid-date - " + x["valid_date"] + " -> Max-temp - " + str(x["max_temp"]) + "C, Min-temp - " + str(x["min_temp"]) + "C, " + x["weather"]["description"])
                        weather_forecast_result = "Tomorrow on " + x["valid_date"] + " you will feel maximum temperature of " + str(x["max_temp"]) + " degrees celcius and minimum temperature of " + str(x["min_temp"]) + " degrees celcius and you can see " + x["weather"]["description"]
                        Mira_talk(weather_forecast_result)

                    else:
                        print("> Valid-date - " + x["valid_date"] + " -> Max-temp - " + str(x["max_temp"]) + "C, Min-temp - " + str(x["min_temp"]) + "C, " + x["weather"]["description"])
                        weather_forecast_result = "On " + x["valid_date"] + " you will feel maximum temperature of " + str(x["max_temp"]) + " degrees celcius and minimum temperature of " + str(x["min_temp"]) + " degrees celcius and you can see " + x["weather"]["description"]
                        Mira_talk(weather_forecast_result)

            elif re.search('tell me about', text):
                topic = text.replace("tell me about ", "")
                if topic:
                    wiki_result = obj.wikipedia(topic)
                    if(wiki_result == False):
                        print("> Sorry. I couldn't load your query from my database. Please try again")
                        Mira_talk("Sorry. I couldn't load your query from my database. Please try again")
                    else:
                        print(">", wiki_result)
                        Mira_talk("According to Wikipedia, " + wiki_result)
                else:
                    print("> Sorry. I couldn't load your query from my database. Please try again")
                    Mira_talk("Sorry. I couldn't load your query from my database. Please try again")

            elif re.search("who is", text):
                topic = text.replace("who is ", "")
                if topic:
                    wiki_result = obj.wikipedia(topic)
                    if(wiki_result == False):
                        print("> Sorry. I couldn't load your query from my database. Please try again")
                        Mira_talk("Sorry. I couldn't load your query from my database. Please try again")
                    else:
                        print(">", wiki_result)
                        Mira_talk("According to Wikipedia, " + wiki_result)
                else:
                    print("> Sorry. I couldn't load your query from my database. Please try again")
                    Mira_talk("Sorry. I couldn't load your query from my database. Please try again")

            elif re.search("what is", text):
                topic = text.replace("what is ", "")
                if topic:
                    wiki_result = obj.wikipedia(topic)
                    if(wiki_result == False):
                        print("> Sorry. I couldn't load your query from my database. Please try again")
                        Mira_talk("Sorry. I couldn't load your query from my database. Please try again")
                    else:
                        print(">", wiki_result)
                        Mira_talk("According to Wikipedia, " + wiki_result)
                else:
                    print("> Sorry. I couldn't load your query from my database. Please try again")
                    Mira_talk("Sorry. I couldn't load your query from my database. Please try again")

            elif "wikipedia" in text or "open wikipedia" in text:
                Mira_talk("Sure, what should I search for you on Wikipedia?")
                while(True):
                    wiki_search = obj.Mira_listen()
                    print(wiki_search.capitalize())
                    if "stop" in wiki_search or "exit" in wiki_search or "close" in wiki_search:
                        Mira_talk("Alright, closing Wikipedia. What else can I do for you?")
                        break
                    elif "tell me about" in wiki_search:
                        wiki_search = wiki_search.replace("tell me about ", "")
                    elif "who is" in wiki_search:
                        wiki_search = wiki_search.replace("who is ", "")
                    wiki_result = obj.wikipedia(wiki_search)
                    if(wiki_result == False):
                        print("> Sorry. I couldn't load your query from my database. Please try again")
                        Mira_talk("Sorry. I couldn't load your query from my database. Please try again")
                    else:
                        print(">", wiki_result)
                        Mira_talk("According to Wikipedia, " + wiki_result)

            elif "news" in text or "headlines" in text:
                news_headlines = obj.news(text)
                print("> ", end="")
                for i in range(5):
                    print(news_headlines[i], end="\n")
                    Mira_talk(news_headlines[i])

            elif "search" in text:
                obj.search_anything_web(text)

            elif ("play" or "hit" in text) and "music" in text:
                pass

            elif ("open" in text or "search" in text or "play" in text) and ("youtube" in text or "video" in text):
                video = text.split(" ")
                play_video = ""
                for x in video:
                    if(x != "open" and x != "play" and x != "search" and x != "on" and x != "in" and x != "youtube"):
                        play_video = play_video + x + " "
                Mira_talk(f"Okay, playing {play_video} on youtube")
                pywhatkit.playonyt(play_video)

            elif ("email" in text or "gmail" in text or "mail" in text) and "send" in text:
                sender_email = config.email
                sender_password = config.email_password

                try:
                    Mira_talk("Whom do you want to email?")
                    recipient = obj.Mira_listen()
                    print(recipient)
                    receiver_email = EMAIL_DIC.get(recipient)
                    if receiver_email:

                        Mira_talk("Can you please tell me the subject?")
                        subject = obj.Mira_listen()
                        print(subject.capitalize())
                        Mira_talk("What is the message?")
                        message = obj.Mira_listen()
                        print(message.capitalize())
                        msg = "Subject: {}\n\n{}".format(subject.capitalize(), message.capitalize())
                        obj.send_mail(sender_email, sender_password, receiver_email, msg)
                        Mira_talk("Your email has been successfully sent")
                        time.sleep(2)

                    else:
                        Mira_talk("Sorry, I coudn't find the requested person's email in my database. Please try again with a different name")

                except:
                    Mira_talk("Sorry. Couldn't send your mail. Please try again")

            elif "capital" in text and "of" in text:
                try:
                    wolfram_alpha_country_capital(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "+" in text or "-" in text or " x " in text or "/" in text or "add" in text or "addition" in text or "subtract" in text or "subtraction" in text or "difference" in text or "multiply" in text or "multiplication" in text or "multiplied" in text or "divide" in text or "division" in text or "divided" in text or "root" in text or "solve" in text or "calculate" in text or "square" in text or "cube" in text:
                try:
                    wolfram_alpha_math_calculation(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "convert" in text and ("into" in text or "to" in text):
                try:
                    wolfram_alpha_unit_conversion(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "gap" in text or "gaps" in text or "how many days" in text or "days" in text:
                if ("monday" or "tuesday" or "wednesday" or "thursday" or "friday" or "saturday") in text:
                    answer = wolfram_alpha_datetime_calculation(text)
                    print(">",answer)
                    Mira_talk("There are "+answer+" between the specified days")
                else:
                    answer = wolfram_alpha_datetime_calculation(text)
                    print(">",answer)
                    Mira_talk("There are "+answer+" between the specified dates")

            elif "historical" in text and "events" in text:
                answer = wolfram_alpha_datetime_calculation(text)
                print(">",answer)
                Mira_talk(answer)

            elif "birthday" in text or "birthdate" in text or "birth date" in text:
                answer = wolfram_alpha_datetime_calculation(text)
                print(">",answer)
                Mira_talk(answer)

            elif "eclipse" in text or "eclipses" in text:
                if "annular" in text:
                    answer = wolfram_alpha_datetime_calculation("eclipse")
                    print(">",answer)
                    print("> Eclipse type: annular")
                    Mira_talk("The upcoming annular eclipse will be visible on "+answer)
                elif "partial" in text:
                    answer = wolfram_alpha_datetime_calculation("eclipses")
                    print(">",answer)
                    print("> Eclipse type: partial")
                    Mira_talk("The upcoming partial eclipse will be visible on "+answer)
                else:
                    answer_annular = wolfram_alpha_datetime_calculation("eclipse")
                    answer_partial = wolfram_alpha_datetime_calculation("eclipses")
                    print(">",answer_annular)
                    print("> Eclipse type: annular")
                    print()
                    print(">",answer_partial)
                    print("> Eclipse type: partial")
                    Mira_talk("The upcoming annular eclipse will be visible on "+answer_annular)
                    Mira_talk("The upcoming partial eclipse will be visible on "+answer_partial)

            elif "january" in text or "february" in text or "march" in text or "april" in text or "may" in text or "june" in text or "july" in text or "august" in text or "september" in text or "october" in text or "november" in text or "december" in text:
                answer = wolfram_alpha_datetime_calculation(text)
                print(">",answer)
                Mira_talk(answer)

            elif "monday" in text or "tuesday" in text or "wednesday" in text or "thursday" in text or "friday" in text or "saturday" in text: #and ("this" in text or "last" in text or "next" in text):
                answer = wolfram_alpha_datetime_calculation(text)
                print(">",answer)
                Mira_talk(answer)

            elif "loan" in text and ("calculate" in text or "calculator" in text):
                try:
                    wolfram_alpha_math_calculation(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif ("balance" in text and ("equation" in text or "reaction" in text)) or "reaction" in text or "reactions" in text or ("speed" in text and "light" in text):
                try:
                    wolfram_alpha_scientific_computations(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif ("calorie" in text or "calories" in text) and ("burn" in text or "burnt" in text):
                try:
                    wolfram_alpha_health_fitness(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "body mass index" in text or "bmi" in text:
                try:
                    wolfram_alpha_health_fitness(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "nutrition" in text or "nutritional facts" in text or "nutrition facts" in text:
                try:
                    wolfram_alpha_health_fitness(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif ("distance" in text and "between" in text) or "geographic coordinates" in text or "coordinates" in text:
                try:
                    wolfram_alpha_geo_info(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "sunrise" in text or "sunset" in text or ("moon" in text and ("phase" in text or "phases" in text)) or "planetary position" in text or "position" in text:
                try:
                    wolfram_alpha_health_fitness(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "am" in text and "drunk" in text:
                try:
                    wolfram_alpha_drinking_check(text)
                except Exception as e:
                    print("> Sorry! I think I did not get what you said and I cannot perform that!\nWhat else can I do for you?")
                    Mira_talk("Sorry! I think I did not get what you said and I cannot perform that. What else can I do for you?")

            elif "what do i have" in text or "do i have plans" in text or "am i busy" in text:
                obj.google_calendar_events(text)

            elif "make a note" in text or "write this down" in text or "remember this" in text:
                Mira_talk("Sure. What would you like me to write down?")
                note_text = obj.Mira_listen()
                print(note_text.capitalize())
                obj.take_note(note_text.capitalize())
                Mira_talk("I've made a note of that")

            elif "close the note" in text or "close notepad" in text:
                Mira_talk("Alright! Closing Notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "chuck norris" in text and "joke" in text:
                cn_json = obj.jokes_chuck_norris()
                print(">",cn_json["value"])
                Mira_talk(cn_json["value"])

            elif "random joke" in text or "joke" in text:
                Mira_talk("You bet! Here's a funny one")
                joke = pyjokes.get_joke()
                print(">", joke)
                Mira_talk(joke)
                # joke_json = obj.jokes_random()
                # print(">",joke_json["setup"])
                # Mira_talk(joke_json["setup"])
                # time.sleep(2)
                # print(">",joke_json["delivery"])
                # Mira_talk(joke_json["delivery"])

            elif "system" in text:
                sys_info = obj.system_info()
                print(">", sys_info)
                Mira_talk(sys_info)

            elif "where is" in text:
                place = text.split("where is ", 1)[1]
                current_loc, target_loc, distance = obj.location(place)
                city = target_loc.get("city", "")
                state = target_loc.get("state", "")
                country = target_loc.get("country", "")
                time.sleep(1)
                try:

                    if city:
                        res = f"{place} is in {state} state and country {country}. It is {distance} km away from your current location"
                        print(">", res)
                        Mira_talk(res)

                    else:
                        res = f"{state} is a state in {country}. It is {distance} km away from your current location"
                        print(">", res)
                        Mira_talk(res)

                except:
                    res = "Sorry, I couldn't get the co-ordinates of the location you requested. Please try again"
                    Mira_talk(res)

            elif "ip address" in text:
                ip = requests.get("https://api.ipify.org").text
                print(">", ip)
                Mira_talk(f"Your ip address is {ip}")

            elif "switch the window" in text or "switch window" in text:
                Mira_talk("Okay, Switching the window")
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "where i am" in text or "current location" in text or "where am i" in text:
                try:
                    city, state, country = obj.my_location()
                    print(">", city, state, country)
                    Mira_talk(f"You are currently in {city} city which is in {state} state and country {country}")
                except Exception as e:
                    Mira_talk("Sorry, I coundn't fetch your current location. Please try again")

            elif "camera" in text or "take a photo" in text or "take a picture" in text or "click a photo" in text or "click a picture" in text or "take a selfie" in text or "click a selfie" in text:
                obj.click_photo()

            elif "take screenshot" in text or "take a screenshot" in text or "capture the screen" in text:
                Mira_talk("By what name do you want to save the screenshot?")
                name = obj.Mira_listen()
                Mira_talk("Alright, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                Mira_talk("The screenshot has been succesfully captured")

            elif "show me the screenshot" in text:
                try:
                    img = Image.open("C:/Users/siddh/OneDrive/Desktop/MIRA")
                    img.show(img)
                    Mira_talk("Here it is")
                    time.sleep(2)

                except IOError:
                    Mira_talk("Sorry, I am unable to display the screenshot")

            elif "hide all files" in text or "hide this folder" in text:
                os.system("attrib +h /s /d")
                Mira_talk("All the files in this folder are now hidden")

            elif "visible" in text or "make files visible" in text:
                os.system("attrib -h /s /d")
                Mira_talk("All the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")

            elif "bitcoin" in text:
                crypto_api = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
                crypto_json = obj.crypto_currency(crypto_api)
                Mira_talk(f"The current price for a Bitcoin is {crypto_json["USD"]} US Dollars")

            elif "ethereum" in text:
                crypto_api = "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD"
                crypto_json = obj.crypto_currency(crypto_api)
                Mira_talk(f"The current price for an Ethereum is {crypto_json["USD"]} US Dollars")

            elif "tether" in text:
                crypto_api = "https://min-api.cryptocompare.com/data/price?fsym=USDT&tsyms=USD"
                crypto_json = obj.crypto_currency(crypto_api)
                Mira_talk(f"The current price for 1 Tether is {crypto_json["USD"]} US Dollars")

            elif "binance coin" in text:
                crypto_api = "https://min-api.cryptocompare.com/data/price?fsym=BNB&tsyms=USD"
                crypto_json = obj.crypto_currency(crypto_api)
                Mira_talk(f"The current price for a Binance Coin is {crypto_json["USD"]} US Dollars")

            elif "solana" in text:
                crypto_api = "https://min-api.cryptocompare.com/data/price?fsym=SOL&tsyms=USD"
                crypto_json = obj.crypto_currency(crypto_api)
                Mira_talk(f"The current price for 1 Solana is {crypto_json["USD"]} US Dollars")

            elif "stock" in text:
                stock_res = obj.stock_market(text)
                print(">", stock_res.info["currentPrice"],"USD")
                Mira_talk("At this moment you can purchase one " + stock_res.info["longName"] + " share for " + str(stock_res.info["currentPrice"]) + " " + stock_res.info["financialCurrency"])

            elif "translate" in text or "translator" in text or "Translate" in text or "Translator" in text:
                Mira_talk("Sure! What do you want me to translate?")
                while(True):
                    text_to_translate = obj.Mira_listen()
                    print(">",text_to_translate.capitalize())
                    if "stop" in text_to_translate or "exit" in text_to_translate or "close" in text_to_translate:
                        Mira_talk("Sure! The translator will be stopped. What else can I do for you?")
                        break
                    else:
                        Mira_talk("To which language you want to translate?")
                        lang = obj.Mira_listen()
                        obj.translate(text_to_translate, lang)
                        Mira_talk("What else do you want me to translate?")

            elif "generate" in text and "password" in text:
                Mira_talk("Sure! Please wait a moment while I create your unique password")
                password = obj.password_generator()
                Mira_talk("Here is your unique password")
                print(">", password)
                Mira_talk("Password is confidential. Make sure you do not share your password with anyone")

            elif "read" in text and "text" in text:
                Mira_talk("Alright, let me read the text for you")
                pasted_text = pyperclip.paste()
                Mira_talk(pasted_text)

            elif "log off" in text or "sign out" in text:
                Mira_talk("Ok , your pc will log off in 10 seconds, make sure you exit from all applications")
                print("> Logging off...")
                time.sleep(10)
                subprocess.call("shutdown", "/l")

            elif "shutdown" in text or "shut down" in text:
                Mira_talk("Ok, your pc will shutdown in 10 seconds. Do you want me to close all the programs before shutting down?")
                shutdown = obj.Mira_listen()
                print(shutdown.capitalize())
                if "yes" in shutdown or "ok" in shutdown or "yeah" in shutdown or "sure" in shutdown or "of course" in shutdown or "ofcourse" in shutdown:
                    Mira_talk("Ok, shutting down...")
                    print("> Shutting down...")
                    time.sleep(10)
                    subprocess.run(['shutdown', '/s', '/t', '0', '/f'], shell=False)
                else:
                    Mira_talk("Ok, however shutting down your pc will automatically close all the programs")
                    print("> Shutting down...")
                    time.sleep(10)
                    subprocess.run(["shutdown", "/s", "/t", "0"])

            elif "restart" in text:
                Mira_talk("Ok , your pc will restart in 10 seconds")
                print("> Restarting...")
                time.sleep(10)
                subprocess.run(["shutdown", "/r", "/t", "0"])

            elif "stop" in text or "close" in text or "exit" in text or "goodbye" in text or "bye" in text:
                if "goodbye" in text or "bye" in text:
                    Mira_talk("It was a pleasure to help you. Your personal assistant Meera is shutting down. Goodbye")
                else:
                    Mira_talk("Alright, going offline. It was a pleasure to help you. I wish you a wonderful day!")
                sys.exit()

            else:
                outputList = []
                Mira_talk("Here are the top 10 search results from Google")
                print(">", end=" ")
                for output in search(text, lang="en", num_results=10, safe="active"):
                    print(output)
                    outputList.append(output)
                Mira_talk("Should I open up the first link for you?")
                query = obj.Mira_listen()
                if "yes" in query or "sure" in query or "ok" in query or "yeah" in query or "ofcourse" in query or "of course" in query:
                    Mira_talk("Here's the first link for you")
                    obj.website_opener(outputList[0])


startExecution = MainThread()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Mira/utils/images/live_wallpaper.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Mira/utils/images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Mira/utils/images/design_2.gif")
        self.ui.label_4.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Mira/utils/images/design_3.gif")
        self.ui.label_5.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Mira/utils/images/design_4.gif")
        self.ui.label_6.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("Mira/utils/images/design_5.gif")
        self.ui.label_7.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
mira = Main()
mira.show()
exit(app.exec_())