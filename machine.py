import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

# Example dataset (you would use your actual dataset here)
data = {
    'loan_amount': [10000, 5000, 15000, 7000, 12000],
    'num_credit_lines': [2, 1, 3, 2, 1],
    'credit_utilization': [30, 40, 60, 25, 35],
    'loan_approved': [1, 0, 1, 0, 1]  # 1 = Approved, 0 = Denied
}

df = pd.DataFrame(data)

# Features and target variable
X = df[['loan_amount', 'num_credit_lines', 'credit_utilization']]
y = df['loan_approved']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model for use in the Flask app
joblib.dump(model, 'loan_model.pkl')

print("Model trained and saved.")
