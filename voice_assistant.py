import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

while True:
    print("Listening")
    text = get_audio()

    if "hello" in text:
        speak("Hello, how are you?")

    elif "fine and you" in text:
        speak("I am doing great")
    
    elif "fine" in text:
        speak("That's great")
