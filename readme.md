## *Project Overview*

### *Credit Risk Evaluation System*

The Credit Risk Evaluation System assesses the creditworthiness of loan applicants using personal, financial, and behavioral data, combined with machine learning for loan prediction.

### *How the Code Works*

#### *Frontend (HTML, CSS, JavaScript)*

The frontend is a web-based form where users provide details like personal information, loan details, travel history, utility payments, social media activity, and e-commerce spending. It uses HTML for structure, CSS for styling, and JavaScript for form handling.

#### *Backend (Flask)*

Built with *Flask, the backend processes form submissions, preprocesses the data, and uses a **Random Forest Classifier* to predict loan approval. The prediction is based on features like loan amount, credit utilization, and payment history.

- *Form Submission:* Sends a POST request to the backend.
- *Data Processing:* Prepares the data for the machine learning model.
- *Prediction:* The model evaluates the loan application and provides a response.

#### *Machine Learning Model*

A *RandomForestClassifier* is trained on historical loan data. The model predicts loan approval or rejection based on the applicant’s information. The model is saved using *joblib* for integration with Flask.

#### *Technologies Used*

- *Frontend:* HTML, CSS, JavaScript
- *Backend:* Flask (Python)
- *Machine Learning:* RandomForestClassifier (Scikit-learn)
- *Model Serialization:* joblib

---

This *Credit Risk Evaluation System* combines a web interface with a machine learning model to predict loan approval based on various data points. The *RandomForestClassifier* ensures accurate predictions for loan eligibility.
