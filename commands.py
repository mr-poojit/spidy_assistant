import subprocess
import os
import webbrowser
import cv2
import yt_dlp

# === Music Player without VLC ===
def play_youtube_audio(search_query):
    print(f"🎵 Searching YouTube for: {search_query}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'noplaylist': True,
        'default_search': 'ytsearch1:',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(search_query, download=False)
        if 'entries' in info:
            info = info['entries'][0]  # first search result
        url = info['url']
        title = info['title']
        print(f"🎶 Now playing: {title}")

        # Play using ffplay (from ffmpeg)
        subprocess.Popen(
            ['ffplay', '-nodisp', '-autoexit', url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

# === Example Command Execution ===
def execute_command(command_text):
    cmd = command_text.lower()

    if "open camera" in cmd:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("❌ Could not open camera.")
            return
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    elif "open browser" in cmd or "start chrome" in cmd:
        webbrowser.open("https://www.google.com")

    elif "open notepad" in cmd:
        subprocess.Popen(["notepad.exe"])

    elif "open calculator" in cmd:
        subprocess.Popen(["calc.exe"])

    elif "open netflix" in cmd or "start netflix" in cmd:
        webbrowser.open("https://www.netflix.com")

    elif "play" in cmd:
        song_name = cmd.replace("play", "").replace("music", "").strip()
        if song_name:
            play_youtube_audio(song_name)
        else:
            play_youtube_audio("lofi hip hop")

    else:
        print("❓ Command not recognized.")
