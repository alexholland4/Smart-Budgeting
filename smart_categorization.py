# (Unfinished) file to automatically categorize new transactions

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

# Step 1: Load data from Excel
data = pd.read_excel('your_data.xlsx')

# Step 2: Feature Engineering (TF-IDF)
tfidf_vectorizer = TfidfVectorizer(max_features=5000, stop_words='english')
X = tfidf_vectorizer.fit_transform(data['Description'])

# Step 3: Data Split
X_train, X_test, y_train, y_test = train_test_split(X, data['Category'], test_size=0.2, random_state=42)

# Step 4: Model Selection (Logistic Regression)
classifier = LogisticRegression(max_iter=1000)

# Step 5: Model Training
classifier.fit(X_train, y_train)

# Step 6: Evaluation (Accuracy)
y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')

# Step 8: Cross-Validation
scores = cross_val_score(classifier, X, data['Category'], cv=5)
print(f'Cross-Validation Scores: {scores}')
