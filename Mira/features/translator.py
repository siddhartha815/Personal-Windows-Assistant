import translators as ts
import gtts as gTTS
import playsound as ps
import os

def Mira_talk(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="en", tld="us")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_hindi(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="hi")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_bengali(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="bn")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_gujarati(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="gu")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_marathi(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="mr")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_tamil(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="ta")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_telugu(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="te")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_malayalam(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="ml")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_kannada(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="kn")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_punjabi(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="pa")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_urdu(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="ur")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_korean(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="ko")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_japanese(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="ja")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_spanish(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="es")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_german(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="de")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_french(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="fr")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_russian(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="ru")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def Mira_talk_chinese(text):
    # create audio data
    file_name = "audio_data.mp3"
    # convert text to speech
    tts = gTTS.gTTS(text=text, lang="zh")
    # save file
    tts.save(file_name)
    try:
        # play file
        ps.playsound(file_name)
    except ps.PlaysoundException as pe:
        print(pe)
    # remove file
    os.remove(file_name)

def translator(text, lang):
    if "hindi" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="hi")
        print(">",translated)
        Mira_talk_hindi(translated)
    
    elif "bengali" in lang or "bangla" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="bn")
        print(">",translated)
        Mira_talk_bengali(translated)

    elif "gujarati" in lang or "gujrati" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="gu")
        print(">",translated)
        Mira_talk_gujarati(translated)

    elif "marathi" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="mr")
        print(">",translated)
        Mira_talk_marathi(translated)

    elif "tamil" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="ta")
        print(">",translated)
        Mira_talk_tamil(translated)

    elif "telugu" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="te")
        print(">",translated)
        Mira_talk_telugu(translated)

    elif "malayalam" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="ml")
        print(">",translated)
        Mira_talk_malayalam(translated)

    elif "kannada" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="kn")
        print(">",translated)
        Mira_talk_kannada(translated)

    elif "punjabi" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="pa")
        print(">",translated)
        Mira_talk_punjabi(translated)

    elif "urdu" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="ur")
        print(">",translated)
        Mira_talk_urdu(translated)

    elif "korean" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="ko")
        print(">",translated)
        Mira_talk_korean(translated)

    elif "japanese" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="ja")
        print(">",translated)
        Mira_talk_japanese(translated)

    elif "spanish" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="es")
        print(">",translated)
        Mira_talk_spanish(translated)

    elif "german" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="de")
        print(">",translated)
        Mira_talk_german(translated)

    elif "french" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="fr")
        print(">",translated)
        Mira_talk_french(translated)

    elif "russian" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="ru")
        print(">",translated)
        Mira_talk_russian(translated)

    elif "chinese" in lang:
        translated = ts.translate_text(text, translator="google", from_language="en", to_language="zh")
        print(">",translated)
        Mira_talk_chinese(translated)

    else:
        Mira_talk("Sorry! I cannot translate to that language. But I support more than 15 languages over the world. You can try them as well!")