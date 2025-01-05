from flask import Flask, request, jsonify
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Define the upload folder for documents
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed extensions for uploaded files
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png', 'txt'}

# Function to check if file extension is allowed
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/submit_credit_risk', methods=['POST'])
def submit_credit_risk():
    try:
        # Extract form data
        name = request.form.get('name')
        gender = request.form.get('gender')
        loan_amount = request.form.get('loanAmount')
        
        # Extract uploaded files
        bank_statement = request.files['bankStatement']
        other_documents = request.files['otherDocuments']
        
        # Ensure files have valid extensions
        if bank_statement and allowed_file(bank_statement.filename):
            bank_statement_filename = secure_filename(bank_statement.filename)
            bank_statement.save(os.path.join(app.config['UPLOAD_FOLDER'], bank_statement_filename))
        
        if other_documents and allowed_file(other_documents.filename):
            other_documents_filename = secure_filename(other_documents.filename)
            other_documents.save(os.path.join(app.config['UPLOAD_FOLDER'], other_documents_filename))
        
        # Process the data and run the model here (use your existing backend code)
        # For example, create a DataFrame with the collected data
        data = {
            'name': name,
            'gender': gender,
            'loan_amount': loan_amount,
            'bank_statement': bank_statement_filename,
            'other_documents': other_documents_filename
        }
        
        # You can perform credit risk prediction or other tasks here
        # For now, just returning the data for testing
        return jsonify({
            'status': 'success',
            'message': 'Form submitted successfully!',
            'data': data
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True)
