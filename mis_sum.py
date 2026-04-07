import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Simple dataset
data = {
    'text': [
        "Drinking hot water cures COVID",
        "Government announces new policy",
        "Aliens landed in India yesterday",
        "Stock market rises today"
    ],
    'label': ['Fake', 'Real', 'Fake', 'Real']
}

df = pd.DataFrame(data)

# Convert text to numbers
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['text'])

# Train model
model = LogisticRegression()
model.fit(X, df['label'])

# Test input
news = ["Chocolate cures all diseases"]

X_test = vectorizer.transform(news)
prediction = model.predict(X_test)

# Simple summary (manual)
summary = "This news claims chocolate cures diseases, which is not scientifically proven."

print("Result:")
print("Prediction:", prediction[0])
print("Summary:", summary)