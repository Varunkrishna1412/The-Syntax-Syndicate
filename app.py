from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(_name_)

# Define the upload folder for documents
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for uploaded files
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'txt'}

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Load your trained model
model = joblib.load('loan_model.pkl')  # Assuming the model is saved in 'loan_model.pkl'

# Preprocessing function (e.g., normalization, encoding)
def preprocess_data(data):
    # For simplicity, let's assume data is already processed
    # You can add preprocessing steps like encoding, scaling here
    scaler = StandardScaler()
    return scaler.fit_transform([data])

# Define the route for submitting credit risk data
@app.route('/api/submit_credit_risk', methods=['POST'])
def submit_credit_risk():
    try:
        # Extract form data
        name = request.form.get('name')
        loan_amount = float(request.form.get('loanAmount'))
        num_credit_lines = int(request.form.get('numOfCreditLines', 0))  # Default to 0 if not provided
        credit_utilization = float(request.form.get('creditUtilization', 0.0))  # Default to 0 if not provided

        # Example: Data collection for prediction
        input_data = [loan_amount, num_credit_lines, credit_utilization]
        
        # Preprocess the data (e.g., scale it)
        processed_data = preprocess_data(input_data)
        
        # Make the prediction
        prediction = model.predict(processed_data)
        
        # Determine the result
        result = "Loan Approved" if prediction == 1 else "Loan Denied"
        
        # Return the result to the frontend
        return jsonify({
            'status': 'success',
            'message': result
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if _name_ == '_main_':
    app.run(debug=True)
