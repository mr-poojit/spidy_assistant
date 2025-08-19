# 🕷️ Spidey Voice Assistant

Spidey is your **personal voice-controlled AI assistant**, inspired by
Siri and JARVIS.\
It listens to wake words like **"Hey Spidey"**, **"Hi Spidey"**, or
**"Yo boy"**, and then executes commands, answers general questions, or
chats with you using AI.

---

## 📹 Demo Video

👉 [Watch the Demo]()

---

## 🚀 Features

- 🎙️ **Wake word activation** ("Hey Spidey", "Hi Spidey", "Yo boy").\
- 🤖 **Command execution** (e.g., open apps, search, system tasks).\
- 💬 **AI-powered conversations** with Ollama integration.\
- 🔊 **Text-to-speech responses** using `pyttsx3`.\
- 🧠 **Speech recognition** using Google Speech API.\
- ⚡ Always-on assistant running in the background.

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mr-poojit/spidy-assistant.git
cd spidey-assistant
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate    # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Assistant

```bash
python main.py
```

---

## 📂 Project Structure

    spidey-assistant/
    ├── main.py # Entry point
    ├── config.py # Global config (name, voice rate, etc.)
    ├── speech/
    │ ├── **init**.py
    │ ├── listener.py # Voice → Text (Vosk)
    │ └── tts.py # Text → Voice (pyttsx3)
    ├── brain/
    │ ├── **init**.py
    │ └── nlp.py # Query handling using LLaMA (Ollama API)
    ├── executor/
    │ ├── **init**.py
    │ └── commands.py # Runs system commands (open apps etc.)
    ├── requirements.txt
    └── README.md

---

## ⚙️ Requirements

- Python **3.8+**
- Working **microphone**
- Internet connection (for Google Speech & Ollama/OpenAI)
- `pip install pyttsx3 speechrecognition`

---

## 📝 Example Interaction

    🎙️ You: Hey Spidey
    💬 Spidey: Hi Master, I'm ready for action!

    🎙️ You: What's the weather today?.
    💬 Spidey: The weather is sunny with mild winds.

    🎙️ You: Open YouTube
    💬 Spidey: Opening YouTube...

---

## 🎥 Future Plans

- Add **GUI with emoji faces** for mood/expressions.\
- Add **Hotkey activation** instead of wake word.\
- Integrate with **home automation** (lights, IoT).

---

## 📹 Demo Link

👉 [Demo Video Here]()

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to
discuss what you'd like to change.

---

## 📜 License

MIT License © 2025 Spidey Assistant

## 👨‍💻 Author

Built with ❤️ by **Poojit Jagadeesh Nagaloti**
