# text_to_speech.py

import pyttsx3
from gtts import gTTS
import playsound
import os
import socket
from googletrans import Translator

# Check if internet is available
def is_connected():
    try:
        socket.create_connection(("1.1.1.1", 53), timeout=2)
        return True
    except:
        return False

# Main function to speak (with language support)
def speak_answer(text, lang='en'):
    print(f"🗣️ Bot is saying ({lang}): {text}")

    if is_connected():
        try:
            if lang != 'en':
                translator = Translator()
                translated = translator.translate(text, dest=lang)
                text = translated.text
                print(f"🌐 Translated to ({lang}): {text}")

            tts = gTTS(text=text, lang=lang)
            tts.save("response.mp3")
            playsound.playsound("response.mp3")
            os.remove("response.mp3")

        except Exception as e:
            print("❌ gTTS failed:", e)
            fallback_offline(text)
    else:
        fallback_offline(text)

# Fallback to offline speaking
def fallback_offline(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        print(" Bol diya ")
    except Exception as e:
        print("❌ pyttsx3 failed:", e)

# ✅ Test Example
if __name__ == "__main__":
    speak_answer("Your legal chatbot is ready to help you.", lang='hi')  # Change 'hi' to 'ta' for Tamil
