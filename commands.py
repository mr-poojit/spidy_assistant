import os
import webbrowser
import subprocess
import signal
import cv2
import pyautogui
import pywhatkit  

def execute_command(query: str):
    query = query.lower()

    # --- SYSTEM COMMANDS ---
    if "open notepad" in query:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad"

    elif "open calculator" in query:
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator"

    elif "open command prompt" in query or "open cmd" in query:
        subprocess.Popen("cmd.exe")
        return "Opening Command Prompt"

    elif "shutdown" in query:
        os.system("shutdown /s /t 1")
        return "Shutting down your PC"

    elif "restart" in query:
        os.system("shutdown /r /t 1")
        return "Restarting your PC"

    # --- CAMERA & SCREENSHOT ---
    elif "open camera" in query:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            return "Error: Could not open camera"
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to quit camera
                break
        cap.release()
        cv2.destroyAllWindows()
        return "Camera closed"

    elif "take screenshot" in query:
        screenshot = pyautogui.screenshot()
        save_path = os.path.join(os.getcwd(), "screenshot.png")
        screenshot.save(save_path)
        return f"Screenshot saved at {save_path}"

    # --- MUSIC ---
    elif "play some music" in query or "play music" in query:
        song = query.replace("play some music", "").replace("play music", "").strip()
        if song:
            pywhatkit.playonyt(song)
            return f"Playing {song} on YouTube"
        else:
            webbrowser.open("https://www.youtube.com/results?search_query=music")
            return "Opening YouTube Music"

    # --- BROWSERS & WEBSITES ---
    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in query:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open gmail" in query:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"

    elif "open github" in query:
        webbrowser.open("https://github.com")
        return "Opening GitHub"

    elif "open chatgpt" in query:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    elif "open linkedin" in query:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    elif "open netflix" in query:
        webbrowser.open("https://netflix.com")
        return "Opening Netflix"

    elif "open whatsapp" in query:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"

    elif "open telegram" in query:
        webbrowser.open("https://web.telegram.org")
        return "Opening Telegram"

    elif "search" in query:
        search_term = query.replace("search", "").strip()
        if search_term:
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            return f"Searching Google for {search_term}"
        return "What should I search?"

    # --- MODES ---
    elif "work mode" in query:
        subprocess.Popen(["notepad.exe"])
        webbrowser.open("https://github.com")
        webbrowser.open("https://mail.google.com")
        webbrowser.open("https://chat.openai.com")
        os.startfile(r"C:\Desktop\Web Development")  # Update to your folder path
        return "Work mode activated: Opened Notepad, VS Code, GitHub, Gmail, ChatGPT, and your Dev folder"

      # Chill Mode
    elif "turn on chill mode" in query:
        # Open the game link and YouTube
        webbrowser.open("https://www.crazygames.com/game/skillwarz")
        webbrowser.open("https://www.youtube.com")
        return "Chill mode on! Game and YouTube are ready, enjoy!"

    return None
