import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("spam.csv")

# Display dataset
print("Dataset:\n")
print(data)

# Input and Output
X = data["text"]
y = data["label"]

# Convert text into numbers using TF-IDF
vectorizer = TfidfVectorizer()

X_vectorized = vectorizer.fit_transform(X)

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Custom message prediction
while True:

    message = input("\nEnter a message: ")

    if message.lower() == "exit":
        print("Program Ended")
        break
    # Convert message into vector
    message_vector = vectorizer.transform([message])

    # Predict
    prediction = model.predict(message_vector)

    print("Prediction:", prediction[0])