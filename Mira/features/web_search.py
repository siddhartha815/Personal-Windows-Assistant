import os
import time
import webbrowser
import gtts,playsound



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


def web_search(command):

    command = command.replace("search ", "")
    tokens = command.split(" ")
    url = "https://www.bing.com/search?pglt=673&q=" + str(tokens[0])
    for i in range(1, len(tokens)):
        url = url + "+" + str(tokens[i])
    url = url + "&cvid=eaf954a8702642e7b494ef6111a946ab&gs_lcrp=EgZjaHJvbWUqBggAEAAYQDIGCAAQABhAMgYIARBFGDkyBggCEAAYQDIGCAMQABhAMgYIBBAAGEAyBggFEC4YQDIGCAYQABhAMgYIBxAAGEAyBggIEAAYQNIBCDI1ODRqMGoxqAIIsAIB&FORM=ANSPA1&PC=ASTS"
    webbrowser.open_new_tab(url)
    Mira_talk("Here is the search results")
    time.sleep(10)