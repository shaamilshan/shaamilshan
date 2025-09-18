import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset (replace with your dataset)
movies = pd.read_csv('movies_dataset.csv')


# Basic preprocessing
movies['genre'] = movies['genre'].fillna('Unknown')
le = LabelEncoder()
movies['genre_encoded'] = le.fit_transform(movies['genre'])

# Select features and target
features = ['budget', 'genre_encoded', 'cast_popularity', 'release_month']
X = movies[features]
y = movies['success']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

