import queue
import sounddevice as sd
import vosk
import json
import threading

model = vosk.Model("models/vosk-model-en-us-0.22")
q = queue.Queue()
listening_paused = False

def _callback(indata, frames, time_, status):
    if status:
        print(status, flush=True)
    if not listening_paused:
        q.put(bytes(indata))

def listen_to_audio():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=_callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "").strip()

def pause_listening():
    global listening_paused
    listening_paused = True

def resume_listening():
    global listening_paused
    listening_paused = False
