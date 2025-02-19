from flask import Flask, render_template, request
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join('model', 'model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        features = [float(request.form[key]) for key in ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup']]
        
        # Reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)[0]

        return render_template('index.html', prediction=f'Predicted Price: ${prediction:.2f}')
    
    except Exception as e:
        return render_template('index.html', error=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
