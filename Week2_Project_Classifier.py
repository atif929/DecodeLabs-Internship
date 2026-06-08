# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    f1_score,
    accuracy_score
)

import pandas as pd


print("=" * 50)
print("Iris Classification Using KNN")
print("=" * 50)

# Load dataset
iris = load_iris()

# Features and target labels
X = iris.data
y = iris.target
labels = iris.target_names

# Create a DataFrame for easier analysis
df = pd.DataFrame(X, columns=iris.feature_names)
df["species"] = [labels[i] for i in y]

print("\nDataset Overview")
print(f"Total Samples : {len(df)}")
print(f"Classes       : {list(labels)}")
print(f"Features      : {list(iris.feature_names)}")

print("\nClass Distribution")
print(df["species"].value_counts().to_string())

print("\nStatistical Summary")
print(df.describe().round(2).to_string())

# Scale features before training KNN
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nFeature Scaling")
print("Method: StandardScaler")
print(
    f"Before scaling - sepal length range: "
    f"{X[:, 0].min():.1f} to {X[:, 0].max():.1f}"
)
print(
    f"After scaling  - sepal length range: "
    f"{X_scaled[:, 0].min():.2f} to {X_scaled[:, 0].max():.2f}"
)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print("\nTrain-Test Split")
print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")

# Find the best value of k
print("\nFinding Optimal K")
print("k  | Accuracy")
print("---|---------")

best_k = 1
best_acc = 0

for k in range(1, 16):
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train, y_train)

    acc = accuracy_score(y_test, knn_temp.predict(X_test))

    if acc > best_acc:
        best_acc = acc
        best_k = k

    print(f"{k:<2} | {acc:.4f}")

print(f"\nSelected K: {best_k}")

# Train the model
model = KNeighborsClassifier(n_neighbors=best_k)
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

print("\nModel Training Complete")
print(f"Training Samples Used: {len(X_train)}")

print("\n" + "=" * 50)
print("Model Evaluation")
print("=" * 50)

# Model accuracy
accuracy = accuracy_score(y_test, predictions)
print(f"\nAccuracy : {accuracy * 100:.2f}%")

# Weighted F1 score
f1 = f1_score(y_test, predictions, average="weighted")
print(f"F1 Score : {f1:.4f}")

# Confusion matrix
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix")
print("(Rows = Actual, Columns = Predicted)")
print(f"{'':12} {'Setosa':>10} {'Versicolor':>12} {'Virginica':>10}")

for i, row_label in enumerate(labels):
    row = f"{row_label:<12}" + "".join(
        f"{cm[i][j]:>10}" for j in range(3)
    )
    print(row)

# Detailed performance metrics
print("\nClassification Report")
print(
    classification_report(
        y_test,
        predictions,
        target_names=labels,
        digits=4
    )
)

print("=" * 50)
print("Sample Predictions")
print("=" * 50)

# Sample flower measurements for testing
test_samples = [
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.7, 5.1, 1.6],
    [6.9, 3.1, 5.4, 2.1]
]

print(f"\n{'Sample':<30} {'Prediction'}")
print("-" * 45)

for sample in test_samples:
    sample_scaled = scaler.transform([sample])
    prediction = model.predict(sample_scaled)[0]
    predicted_label = labels[prediction]

    print(f"{str(sample):<30} {predicted_label}")

print("")
print("Project Completed")