import webbrowser, urllib, re
import urllib.parse
import urllib.request
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

domain = input("Enter the song name: ")
song = urllib.parse.urlencode({"search_query" : domain})
print("> Song" + song)

result = urllib.request.urlopen("http://www.youtube.com/results?" + song)
print(">", result)

search_results = re.findall(r'href=\"\/watch\?v=(.{4})', result.read().decode())
print(">", search_results)

url = "http://www.youtube.com/watch?v="+str(search_results)

Mira_talk("Playing " + domain)
webbrowser.open_new(url)