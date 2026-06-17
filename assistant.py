# assistant.py — Main entry point

import datetime
from speech_engine import speak, listen
from command_handler import handle_command

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning! I am your Personal Voice Assistant.")
    elif 12 <= hour < 17:
        speak("Good Afternoon! I am your Personal Voice Assistant.")
    else:
        speak("Good Evening! I am your Personal Voice Assistant.")
    speak("How can I help you? Say exit or bye to quit.")

def main():
    greet()
    running = True
    while running:
        command = listen()
        if command:
            running = handle_command(command)
        else:
            print("No command detected, listening again...")

if __name__ == "__main__":
    main()
