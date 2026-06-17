# speech_engine.py — Listen & Speak

import pyttsx3
import speech_recognition as sr

# ── Text to Speech ───────────────────────────────────────────
engine = pyttsx3.init()
engine.setProperty('rate', 170)      # Speed
engine.setProperty('volume', 1.0)    # Volume

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0=Male, 1=Female

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# ── Speech to Text ───────────────────────────────────────────
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Internet connection error.")
            return ""