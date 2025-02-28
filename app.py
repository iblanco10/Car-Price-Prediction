from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load("car_price_model.pkl")

# Mapping categorical values
fuel_mapping = {"Petrol": 0, "Diesel": 1, "Electric": 2, "Hybrid": 3}
transmission_mapping = {"Manual": 0, "Automatic": 1, "Semi-Automatic": 2}

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction API route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert categorical inputs
        fuel_type = fuel_mapping.get(data["Fuel_Type"], 0)
        transmission = transmission_mapping.get(data["Transmission"], 0)

        # Extract features
        features = np.array([
            data["Year"],
            data["Engine_Size"],
            data["Mileage"],
            data["Doors"],
            data["Owner_Count"],
            fuel_type,
            transmission
        ]).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Return prediction as JSON
        return jsonify({"Predicted Price": round(prediction[0], 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

