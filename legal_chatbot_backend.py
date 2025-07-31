from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# NLTK setup
nltk.download('punkt')
nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

# Initialize Flask app
app = Flask(__name__)

# ✅ Add homepage route for browser
@app.route("/")
def home():
    return "✅ Legal Chatbot backend is running!"

# Load dataset
with open("legal_dataset (1).json", "r", encoding="utf-8") as f:
    dataset = json.load(f)

# Load sentence transformer model
embedder = SentenceTransformer('all-MiniLM-L6-v2')

# Preprocessing
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS and t not in string.punctuation]
    return " ".join(tokens)

# Predict best matching intent using cosine similarity
def predict_intent(user_input):
    user_embedding = embedder.encode(user_input, convert_to_tensor=True)
    best_match = None
    best_score = -1

    for item in dataset:
        q_embedding = embedder.encode(item["question"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(user_embedding, q_embedding).item()
        if score > best_score:
            best_score = score
            best_match = item

    return best_match["intent"] if best_match else None

# Get best matching answer for predicted intent
def get_answer(intent, user_input):
    candidates = [item for item in dataset if item["intent"] == intent]
    if not candidates:
        return "Maaf kijiye, mujhe is prashn ka uttar nahi mila."

    user_embedding = embedder.encode(user_input, convert_to_tensor=True)
    best_match = None
    best_score = -1

    for item in candidates:
        q_embedding = embedder.encode(item["question"], convert_to_tensor=True)
        score = util.pytorch_cos_sim(user_embedding, q_embedding).item()
        if score > best_score:
            best_score = score
            best_match = item

    return best_match["answer"] if best_match else "Maaf kijiye, mujhe is prashn ka uttar nahi mila."

# ✅ API endpoint
@app.route("/get_legal_answer", methods=["POST"])
def get_legal_answer():
    data = request.get_json()
    user_query = data.get("query")

    if not user_query:
        return jsonify({"error": "Query is missing"}), 400

    intent = predict_intent(user_query)
    answer = get_answer(intent, user_query)

    return jsonify({
        "intent": intent,
        "answer": answer
    })

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
