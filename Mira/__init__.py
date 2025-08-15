import speech_recognition as sr
import gtts, playsound, os

from Mira.features import date_time
from Mira.features import appopener
from Mira.features import web_browser
from Mira.features import weather
from Mira.features import wikipedia
from Mira.features import news
from Mira.features import send_email
from Mira.features import web_search
from Mira.features import google_calendar
from Mira.features import note
from Mira.features import system_stats
from Mira.features import loc
from Mira.features import click_photo
from Mira.features import cryptocurrency
from Mira.features import jokes
from Mira.features import stock_market
from Mira.features import translator
from Mira.features import generate_password


class MiraAssistant:
    def __init__(self):
        pass

    def Mira_listen(self):
        # create recogner
        recognizer = sr.Recognizer()
        # what we speak into the microphone should be our source
        with sr.Microphone() as source:
            print("> Listening...")
            # use the listen function so the recognizer can catch the source (our mic)
            audio = recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, phrase_time_limit=10)
            text = ""
            try:
                text = recognizer.recognize_google(audio, language="en-US")
                while(text == ""):
                    audio = recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source, phrase_time_limit=10)
            except sr.RequestError as re:
                print(re)
            except sr.UnknownValueError as uve:
                print(uve)
            except sr.WaitTimeoutError as wte:
                print(wte)

        text = text.lower()
        return text
    

    def Mira_talk(self, text):
        # create audio data
        file_name = "audio_data.mp3"
        # convert text to speech
        tts = gtts.gTTS(text=text, lang="en", tld="us")
        # save file
        tts.save(file_name)
        try:
            # play file
            playsound.playsound(file_name)
        except playsound.PlaysoundException as pe:
            print(pe)
        # remove file
        os.remove(file_name)

        # # using pyttsx3
        # engine.say(text)
        # engine.runAndWait()

    def tell_me_date(self):

        return date_time.date()
    
    def tell_me_time(self):

        return date_time.time()
    
    def tell_me_month(self):

        return date_time.month()
    
    def tell_me_year(self):

        return date_time.year()
    
    def tell_me_weekday(self):

        return date_time.weekday()
    
    def open_any_app(self, app_name):

        return appopener.open_desktop_app(app_name)
    
    def close_any_app(self, app_name):

        return appopener.close_desktop_app(app_name)
    
    def website_opener(self, domain):

        return web_browser.website_opener(domain)
    

    def current_weather(self, city):

        return weather.get_current_weather(city)
    
    def weather_forecast(self, city):

        return weather.get_weather_forecast(city)
    
    def wikipedia(self, topic):

        return wikipedia.wikipedia_info(topic)
    
    def news(self, text):

        return news.get_news(text)
    
    def send_mail(self, sender_email, sender_password, receiver_email, msg):

        return send_email.mail(sender_email, sender_password, receiver_email, msg)
    
    def google_calendar_events(self, text):
        service = google_calendar.authenticate_google()
        date = google_calendar.get_date(text)

        if date:
            return google_calendar.get_events(date, service)
        else:
            pass

    def search_anything_web(self, command):
        web_search.web_search(command)

    def take_note(self, text):
        note.note(text)

    def system_info(self):
        return system_stats.system_stats()
    
    def location(self, location):
        current_loc, target_loc, distance = loc.loc(location)
        return current_loc, target_loc, distance
    
    def my_location(self):
        city, state, country = loc.my_location()
        return city, state, country
    
    def click_photo(self):
        click_photo.take_a_photo()

    def crypto_currency(self, crypto_api):

        return cryptocurrency.cryptocurrency(crypto_api)
    
    def jokes_chuck_norris(self):

        return jokes.chuck_norris_jokes()
    
    def jokes_random(self):

        return jokes.random_jokes()
    
    def stock_market(self, text):
        
        return stock_market.get_stock_price(text)
    
    def translate(self, input, lang):
        
        translator.translator(input, lang)

    def password_generator(self):
        return generate_password.generate_password()