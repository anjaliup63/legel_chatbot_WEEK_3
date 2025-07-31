# speech_to_text.py
import speech_recognition as sr

def get_voice_input():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Bolna shuru karo...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='en-IN')
        print("📝 Tumne kaha:", text)
        return text
    except sr.UnknownValueError:
        print("❌ Maaf karo, mai samajh nahi paya.")
        return ""
    except sr.RequestError:
        print("🚫 Speech service error.")
        return ""

# 👇 This part is missing in your file — add this to run the function!
if __name__ == "__main__":
    get_voice_input()
