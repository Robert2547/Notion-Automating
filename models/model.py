import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from joblib import dump


# Define file paths
status_file = 'models/email_labels/Status.csv'
application_file = 'models/email_labels/Application.csv'
joblist_file = 'models/email_labels/Joblist.csv'

# Load each dataset
status_emails = pd.read_csv(status_file)
application_emails = pd.read_csv(application_file)
joblist_emails = pd.read_csv(joblist_file)

# Combine the datasets
all_emails = pd.concat([status_emails, application_emails, joblist_emails], ignore_index=True)

# Save the combined dataset to a CSV file
all_emails.to_csv('models/combined_emails.csv', index=False)

# Vectorize the 'Email Content' text data
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(all_emails['Email Content'])
y = all_emails['Category']

# Split the dataset into training and remaining data (70% training, 30% remaining)
X_train, X_remaining, y_train, y_remaining = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Split the remaining data equally into validation and testing sets (15% each)
X_validation, X_test, y_validation, y_test = train_test_split(
    X_remaining, y_remaining, test_size=0.5, random_state=42)

# Train the model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model on the validation set
validation_predictions = model.predict(X_validation)
print("Validation Set Evaluation:")
print(classification_report(y_validation, validation_predictions))

# Evaluate the model on the test set (Final Evaluation)
test_predictions = model.predict(X_test)
print("Test Set Evaluation:")
print(classification_report(y_test, test_predictions))

# Save the model and vectorizer
dump(model, 'email_classifier_model.joblib')
dump(vectorizer, 'vectorizer.joblib')