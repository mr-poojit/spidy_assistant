import pyttsx3
import time
from speech.listener import pause_listening, resume_listening

engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    if not text:
        return
    pause_listening()  # stop mic while speaking
    engine.stop()
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)  # small delay to avoid self-pickup
    resume_listening()
