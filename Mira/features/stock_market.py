import os
import gtts, playsound
import speech_recognition as sr
import yfinance as yf

def Mira_listen():
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

def Mira_talk(text):
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

def get_stock_price(text):
    if "apple" in text and "stock" in text:
        apple = yf.Ticker("AAPL")
        return apple

    # Stocks - Facebook/WhatsApp/Instagram/Meta
    elif ("facebook" or "whatsapp" or "instagram" or "meta") in text and "stock" in text:
        meta = yf.Ticker("META")
        return meta

    # Stocks - Tesla
    elif "tesla" in text and "stock" in text:
        tesla = yf.Ticker("TSLA")
        return tesla

    # Stocks - TCS
    elif ("tata" in text or "tcs" in text or "tata consultancy service" in text) and "stock" in text:
        tcs = yf.Ticker("TCS.NS")
        return tcs

    # Stocks - Hindustan Unilever
    elif "hindustan unilever" in text and "stock" in text:
        hul = yf.Ticker("HINDUNILVR.NS")
        return hul
        
    # Stocks - Infosys
    elif "infosys" in text and "stock" in text:
        infosys = yf.Ticker("INFY.NS")
        return infosys

    # Stocks - HDFC Bank
    elif "hdfc bank" in text and "stock" in text:
        hdfc = yf.Ticker("HDFCBANK.NS")
        return hdfc

    # Stocks - Reliance Industries
    elif "reliance" in text and "stock" in text:
        reliance = yf.Ticker("RELIANCE.NS")
        return reliance

    # Stocks - Bajaj Finance
    elif "bajaj finance" in text and "stock" in text:
        bf = yf.Ticker("BAJFINANCE.NS")
        return bf

    # Stocks - Larsen & Toubro
    elif ("larsen" in text or "toubro" in text) and "stock" in text:
        lt = yf.Ticker("LT.NS")
        return lt

    # Stocks - ITC
    elif "itc" in text and "stock" in text:
        itc = yf.Ticker("ITC.NS")
        return itc

    # Stocks - ICICI Bank
    elif "icici" in text and "stock" in text:
        icici = yf.Ticker("ICICIBANK.NS")
        return icici

    # Stocks - Godrej Consumer Products
    elif "godrej" in text and "stock" in text:
        godrej = yf.Ticker("GODREJCP.NS")
        return godrej
    
    # Stocks - Any other stock price
    else:
        Mira_talk("Excuse me! Can you please tell me the stock symbol?")
        try:
            stock_symbol = Mira_listen()
            print(stock_symbol)
            stock = yf.Ticker(stock_symbol.upper())

            return stock
        except Exception as e:
            Mira_talk("Sorry! I did not get that. Can you please type the stock symbol for me?")
            stock_symbol = input("> Type here: ")
            stock = yf.Ticker(stock_symbol.upper())

            return stock