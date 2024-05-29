from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Example data and labels
data = ["good service", "bad quality", "excellent product", "poor experience"]
labels = [1, 0, 1, 0]  # 1 for positive, 0 for negative

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data)
y = labels

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
