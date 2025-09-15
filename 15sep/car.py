import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

columns = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df = pd.read_csv(r"C:\shaamilshan\15sep\car.data", names=columns)

print("Dataset Info:\n")
print(df.info())
print("\nMissing values per column:\n", df.isnull().sum())


print("\nClass distribution:\n", df['class'].value_counts())

label_encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


X = df.drop(columns="class")
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


y_pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))


cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=label_encoders["class"].classes_,
            yticklabels=label_encoders["class"].classes_)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


probs = model.predict_proba(X_test)
print("\nSample predictions with probabilities:")
for i in range(10):
    pred_class = label_encoders["class"].inverse_transform([y_pred[i]])[0]
    prob_str = ", ".join(f"{cls}:{prob:.2f}" for cls, prob in zip(label_encoders["class"].classes_, probs[i]))
    print(f"Input: {X_test.iloc[i].tolist()}, Predicted: {pred_class}, Probabilities: {prob_str}")


print("\nCar Evaluation Prediction ----")

def encode_input(col, val):
    le_col = label_encoders[col]
    try:
        return int(le_col.transform([val])[0])
    except ValueError:
        print(f"Value '{val}' not recognized for {col}. Allowed values: {list(le_col.classes_)}")
        exit()

# Get user input
buying = encode_input("buying", input("Enter buying price (vhigh, high, med, low): ").strip())
maint = encode_input("maint", input("Enter maintenance cost (vhigh, high, med, low): ").strip())
doors = encode_input("doors", input("Enter number of doors (2, 3, 4, 5more): ").strip())
persons = encode_input("persons", input("Enter capacity in persons (2, 4, more): ").strip())
lug_boot = encode_input("lug_boot", input("Enter luggage boot size (small, med, big): ").strip())
safety = encode_input("safety", input("Enter safety level (low, med, high): ").strip())

# Predict
user_features = [[buying, maint, doors, persons, lug_boot, safety]]
print("Encoded user input features:", user_features)

prediction = model.predict(user_features)[0]
predicted_label = label_encoders["class"].inverse_transform([prediction])[0]

print(f"\nPrediction: {predicted_label}")
