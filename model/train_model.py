import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from utils.preprocess import load_data, clean_data, split_data

# Load and clean data
df = load_data()
df = clean_data(df)

# Split into X and y
X, y = split_data(df)

# Split into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Define models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "KNN": KNeighborsClassifier(),
    "SVM": SVC(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier()
}

best_model = None
best_score = 0

print("\nModel Comparison:\n")

# Train and evaluate all models
for name, model in models.items():
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)

    print(f"{name}: {score:.4f}")

    if score > best_score:
        best_score = score
        best_model = model

print("\nBest Model:", best_model)
print("Best Accuracy:", best_score)

# Save best model
with open("model/rf_model.pkl", "wb") as f:
    pickle.dump(best_model, f)