import os
import webbrowser
import subprocess

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

    elif "open linkedin" in query:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"

    elif "search" in query:
        search_term = query.replace("search", "").strip()
        if search_term:
            webbrowser.open(f"https://www.google.com/search?q={search_term}")
            return f"Searching Google for {search_term}"
        return "What should I search?"

    # --- MULTIPLE TASKS (CHAINED) ---
    elif "work mode" in query:
        subprocess.Popen(["notepad.exe"])
        subprocess.Popen(["calc.exe"])
        webbrowser.open("https://github.com")
        webbrowser.open("https://mail.google.com")
        return "Opened Notepad, Calculator, GitHub, and Gmail for work mode"

    return None
