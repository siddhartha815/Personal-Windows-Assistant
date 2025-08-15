import cv2
import gtts, playsound, os
import speech_recognition as sr

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

def take_a_photo():
    Mira_talk("Sure! Get ready for a great photo!")

    cam = cv2.VideoCapture(0)

    ret, image = cam.read()

    if ret:
        Mira_talk("The photo has been taken successfully")
        Mira_talk("By what name do you want to save the photo?")
        name = Mira_listen()
        print(">", name)

        cv2.imwrite(f"{name}.png", image)
        Mira_talk("The photo has been saved successfully")

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        img = cv2.imread(f"{name}.png")

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        Mira_talk("Here is your captured image")
        cv2.imshow("Captured Image", img)

        Mira_talk("You can press any key to close the window")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("> No image detected. Please try again.")
        Mira_talk("Sorry! No image detected. To click a photo, you can say - 'take a photo'")

    cam.release()