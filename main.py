import speech_recognition as sr
import pyttsx3
from commands import execute_command, ask_ollama
from ollama_integration import process_query


def speak(text):
    """Convert text to speech and print"""
    print(f"💬 Spidey says: {text}")
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 175)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("Voice error:", e)


def listen():
    """Listen through mic and return recognized text"""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"🔊 Heard: {text}")
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return ""


def run_assistant():
    """Main assistant loop"""
    while True:
        print("🎙️ Waiting for wake word: 'Hey Spidey', 'Hi Spidey', 'Yo boy'...")
        wake = listen()

        if "hey spidey" in wake or "hi spidey" in wake or "yo boy" in wake:
            speak("Hi Master, I'm ready for action!")

            while True:
                query = listen()

                if query in ["quit", "exit", "stop"]:
                    speak("Spidey shutting down. See you soon!")
                    return

                if not query:
                    continue

                # Try built-in command execution
                response = execute_command(query)
                if response:
                    speak(response)
                    continue

                # Otherwise process with Ollama/LLM
                ai_response = process_query(query) or ask_ollama(query)
                if ai_response:
                    speak(ai_response)


if __name__ == "__main__":
    run_assistant()
