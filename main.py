import speech_recognition as sr
import pyttsx3
from commands import execute_command
from ollama_integration import process_query

# Initialize TTS
engine = pyttsx3.init()
engine.setProperty('rate', 175)
engine.setProperty('volume', 1.0)

def speak(text):
    print(f"💬 Spidey says: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Spidey is now listening... Say 'quit' to exit.")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🔊 Heard: {text}")
        return text.lower()
    except sr.UnknownValueError:
        print("❌ I didn't catch that.")
        return ""
    except sr.RequestError:
        print("❌ Speech service error.")
        return ""

def run_assistant():
    while True:
        query = listen()
        if query in ["quit", "exit", "stop"]:
            speak("Spidey shutting down. See you soon!")
            break

        if not query:
            continue

        # Let Ollama or AI model process it
        ai_response = process_query(query)
        if ai_response:
            speak(ai_response)

        # Try to execute OS-level command
        execute_command(query)

if __name__ == "__main__":
    run_assistant()
