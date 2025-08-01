# -*- coding: utf-8 -*-
"""intent_classifier_82.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R8BKfSOzi66-VNMQFzDmo-AggKi2y5pN
"""

!pip install nltk sentence-transformers scikit-learn pandas --quiet

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import json
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sentence_transformers import SentenceTransformer
import pickle

from google.colab import files
uploaded = files.upload()

with open('legal_dataset (1).json', 'r') as f:
    data = json.load(f)

questions = [item['question'] for item in data]
intents = [item['intent'] for item in data]

X_train, X_test, y_train, y_test = train_test_split(
    questions, intents, test_size=0.2, random_state=42, stratify=intents)

model = SentenceTransformer('all-MiniLM-L6-v2')
X_train_embed = model.encode(X_train, show_progress_bar=True)
X_test_embed = model.encode(X_test, show_progress_bar=True)

clf = RandomForestClassifier(n_estimators=300, random_state=42)
clf.fit(X_train_embed, y_train)

y_pred = clf.predict(X_test_embed)
print("✅ Accuracy:", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))

with open("intent.pkl", "wb") as f:
    pickle.dump(clf, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(model, f)  # actually saving SentenceTransformer model, not TFIDF

files.download("intent.pkl")
files.download("vectorizer.pkl")







