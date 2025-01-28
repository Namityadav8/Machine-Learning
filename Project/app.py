from flask import Flask, render_template, request
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load("Project\heart_disease_prediction_model.pkl")



# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Render the frontend

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = int(request.form['age'])
        cp = int(request.form['cp'])
        thalach = int(request.form['thalach'])

        # Create DataFrame for input data
        user_data = pd.DataFrame([[age, cp, thalach]], columns=['age', 'cp', 'thalach'])

        # Predict using the model
        prediction = model.predict(user_data)

        # Prepare the result
        result = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease Detected"
    except Exception as e:
        result = f"Error: {e}"

    return render_template('index.html', prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
