# command_handler.py — Map commands to actions

import webbrowser
import datetime
import wikipedia
import pywhatkit
from speech_engine import speak

def handle_command(command):

    # ── Time ─────────────────────────────────────────────────
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {time}")

    # ── Date ─────────────────────────────────────────────────
    elif "date" in command:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {date}")

    # ── Search Web ───────────────────────────────────────────
    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    # ── Play YouTube ─────────────────────────────────────────
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    # ── Wikipedia ────────────────────────────────────────────
    elif "who is" in command or "what is" in command:
        topic = command.replace("who is", "").replace("what is", "").strip()
        speak(f"Searching Wikipedia for {topic}")
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't find information on that.")

    # ── Open Apps ────────────────────────────────────────────
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")

    # ── Joke ─────────────────────────────────────────────────
    elif "joke" in command:
        speak("Why do programmers prefer dark mode? Because light attracts bugs!")

    # ── Greeting ─────────────────────────────────────────────
    elif "hello" in command or "hi" in command:
        speak("Hello! How can I help you today?")

    # ── Exit ─────────────────────────────────────────────────
    elif "exit" in command or "quit" in command or "bye" in command:
        speak("Goodbye! Have a great day!")
        return False

    # ── Unknown ──────────────────────────────────────────────
    else:
        speak("Sorry, I didn't understand that. Please try again.")

    return True