from flask import Flask, request, render_template
import numpy as np
import joblib
# Use the complete path to where the model file is stored
model = joblib.load('E:\SGP/rf_model.pkl')
scaler = joblib.load('E:\SGP\scaler.pkl')



import os
print(os.path.exists('rf_model.pkl'))  # Should print True if the file is correctly placed


app = Flask(__name__)



@app.route('/')

def home():
    return render_template('index.html')  # Render index.html

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the form data and convert it to a list of floats
        input_features = [float(x) for x in request.form.values()]
        features = np.array(input_features).reshape(1, -1)

        # Scale the features
        features_scaled = scaler.transform(features)

        # Predict using the model
        prediction = model.predict(features_scaled)

        # Result interpretation
        result = "You may have diabetes." if prediction[0] == 1 else "You are not likely to have diabetes."
        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
