import requests
import gtts, playsound, os



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



news_api_key = "{Your news API key goes here}"



def get_news(text):
    if "us" in text or "united states" in text or "america" in text:
        Mira_talk("Alright, here are the top five headlines from US across the web.")
        news_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + news_api_key
        news = requests.get(news_url).json()
        articles = news["articles"]
        news_headlines = []
        for x in articles:
            news_headlines.append(x["title"])
        return news_headlines
    
    elif "france" in text:
        Mira_talk("Alright, here are the top five headlines from France across the web.")
        news_url = "https://newsapi.org/v2/top-headlines?country=fr&apiKey=" + news_api_key
        news = requests.get(news_url).json()
        articles = news["articles"]
        news_headlines = []
        for x in articles:
            news_headlines.append(x["title"])
        return news_headlines

    elif "germany" in text or "german" in text:
        Mira_talk("Alright, here are the top five headlines from Germany across the web.")
        news_url = "https://newsapi.org/v2/top-headlines?country=de&apiKey=" + news_api_key
        news = requests.get(news_url).json()
        articles = news["articles"]
        news_headlines = []
        for x in articles:
            news_headlines.append(x["title"])
        return news_headlines

    elif "canada" in text:
        Mira_talk("Alright, here are the top five headlines from Canada across the web.")
        news_url = "https://newsapi.org/v2/top-headlines?country=ca&apiKey=" + news_api_key
        news = requests.get(news_url).json()
        articles = news["articles"]
        news_headlines = []
        for x in articles:
            news_headlines.append(x["title"])
        return news_headlines

    elif "italy" in text:
        Mira_talk("Alright, here are the top five headlines from Italy across the web.")
        news_url = "https://newsapi.org/v2/top-headlines?country=it&apiKey=" + news_api_key
        news = requests.get(news_url).json()
        articles = news["articles"]
        news_headlines = []
        for x in articles:
            news_headlines.append(x["title"])
        return news_headlines

    # elif "india" in text or "indian" in text:
    #     news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + news_api_key
    #     news = requests.get(news_url).json()
    #     articles = news["articles"]
    #     news_headlines = []
    #     for x in articles:
    #         news_headlines.append(x["title"])
    #     return news_headlines
    
    else:
        Mira_talk("Alright, here are the top five headlines from India across the web.")
        news_url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=" + news_api_key
        news = requests.get(news_url).json()
        articles = news["articles"]
        news_headlines = []
        for x in articles:
            news_headlines.append(x["title"])
        return news_headlines