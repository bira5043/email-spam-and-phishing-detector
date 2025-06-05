import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Sample dataset
data = {
    "text": [
        "You have won a $1000 prize, click to claim!",
        "Urgent: Update your bank details now.",
        "Hello, meeting at 3 PM today.",
        "Here is the project file for review.",
        "Verify your account or it will be locked.",
        "Free access to exclusive content!",
        "This is a phishing scam to steal login info.",
    ],
    "label": ["spam", "phishing", "ham", "ham", "phishing", "spam", "phishing"]
}
df = pd.DataFrame(data)

# Vectorization
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# Model
model = MultinomialNB()
model.fit(X, y)

# Save
joblib.dump(model, "spam_phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
