from speech.listener import listen_to_audio
from speech.tts import speak
from brain.nlp import process_query

def run_assistant():
    speak("Yes Master, I am Spidey.")
    while True:
        text = listen_to_audio()
        if not text:
            continue
        intent, reply = process_query(text)
        speak(reply)
        if intent == "exit":
            speak("Goodbye!")
            break