import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from joblib import dump

from models.csv import load_csv


def model_main(service):

    all_emails = pd.read_csv("models/combined_emails.csv")

    # Vectorize the 'Email Content' text data
    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(all_emails["Email Content"])
    y = all_emails["Category"]

    # Split the data into training and remaining sets (70% and 30%)
    X_train, X_remaining, y_train, y_remaining = train_test_split(
        X, y, test_size=0.35, random_state=42
    )
    # Split the remaining data equally into validation and testing sets (15% each)
    X_validation, X_test, y_validation, y_test = train_test_split(
        X_remaining, y_remaining, test_size=0.5, random_state=42
    )

    # Train the model
    model = MultinomialNB()
    model.fit(X_train, y_train)
    print("Successfully trained model")

    # Evaluate the model on the validation set
    validation_predictions = model.predict(X_validation)
    print("Validation Set Evaluation:")
    print(classification_report(y_validation, validation_predictions))

    # Evaluate the model on the test set (Final Evaluation)
    test_predictions = model.predict(X_test)
    print("Test Set Evaluation:")
    print(classification_report(y_test, test_predictions))

    # Save the model and vectorizer
    dump(model, "email_classifier_model.joblib")
    dump(vectorizer, "vectorizer.joblib")
