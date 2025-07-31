# legel_chatbot_WEEK_3

This project is a voice-based legal chatbot built using Python and Flask. It accepts queries via voice or text, detects language (English or Hinglish), predicts legal intent, and responds with accurate legal answers in text and audio.

## Features

- Accepts voice or text queries
- Detects user intent using sentence similarity
- Speaks answer using text-to-speech
- Supports Hinglish questions and translates replies
- Backend API built using Flask
- Expandable question-answer dataset in JSON

## Project Structure

legal_chatbot_backend.py - Flask API  
voice_chatbot.py - Voice chatbot logic  
legal_dataset (1).json - Legal question-answer data  
speech_to_text.py - Voice input handling  
text_to_speech.py - Voice output handling  
requirements.txt - Python dependencies  
README.md - Project documentation

## Setup Instructions

1. Clone the repository  
git clone https://github.com/yourusername/legal-voice-chatbot.git  
cd legal-voice-chatbot

2. Create a virtual environment (optional)  
python -m venv venv  
venv\Scripts\activate

3. Install dependencies  
pip install -r requirements.txt

4. Windows users should install pyaudio using pipwin  
pip install pipwin  
pipwin install pyaudio

## Running the Chatbot

1. Start the backend server  
python legal_chatbot_backend.py  
You should see "Legal Chatbot backend is running!" in the terminal

2. Start the voice chatbot  
python voice_chatbot.py  
Type or speak your legal question

## Example

User: Mere bhai ne mujhe maara hai  
Intent: domestic_violence_family  
Bot Reply: Family ke dwara hinsa bhi Domestic Violence Act me aati hai. Aap police ya Mahila Aayog se sampark karein.  

## How It Works

1. Converts voice to text using SpeechRecognition  
2. Detects Hinglish using keywords  
3. Finds best matching question using SentenceTransformer  
4. Predicts intent  
5. Retrieves best matching answer  
6. Translates if required using googletrans  
7. Converts answer to speech using gTTS

## Customizing the Dataset

Open the file legal_dataset (1).json and add your own Q&A like this:  
{  
  "intent": "cybercrime",  
  "question": "Instagram pe dhamki mil rahi hai",  
  "answer": "Aap cybercrime.gov.in par report file kar sakte hain."  
}

Restart the backend after editing the file.

## Requirements

Python 3.8+  
Internet connection for speech and translation  
Mic and speaker for voice features  
See requirements.txt for full list of packages

## Future Scope

Add support for more languages  
Deploy to web or mobile app  
Enable GPT fallback when no intent matches  
Store chat history

## License

This project is open for educational and non-commercial use. Please credit the original developer if reused.

## Author

Anjali Upadhyay  
B.Tech CSE | AI/ML and Web Development Projects  
Tools: Python, Flask, Sentence Transformers, HuggingFace, Google Colab  
Projects: Health Chatbot, SMS Spam Detector, Legal Voice Chatbot  
