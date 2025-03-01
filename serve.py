from flask import Flask, request, jsonify
import joblib
import os

# Initialize Flask app
app = Flask(__name__)

# Define the model path
model_path = "/opt/ml/model/model.pkl"

# Function to load the model
def load_model():
    global model, expected_features
    if os.path.exists(model_path):
        with open(model_path, 'rb') as f:
            model = joblib.load(f)
        expected_features = model.n_features_in_  # Get the number of features the model expects
    else:
        model = None
        expected_features = None

# Load the model when the app starts
load_model()

# Health check route
@app.route("/ping", methods=["GET"])
def ping():
    """Health check route to verify the server is running."""
    status = 200 if model is not None else 500
    return jsonify({"status": "ok" if model else "error"}), status

# Home route (to confirm the server is running)
@app.route("/", methods=["GET"])
def home():
    """Simple route to confirm the server is running."""
    return "Server is running!", 200

# Prediction route
@app.route("/invocations", methods=["POST"])
def predict():
    """Receives JSON input and returns a prediction."""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        # Get JSON data from request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        # Convert input to list of values
        features = list(data.values())

        # Validate number of features
        if len(features) != expected_features:
            return jsonify({"error": f"Expected {expected_features} features, but got {len(features)}"}), 400

        # Convert to 2D array for model prediction
        features = [features]  
        prediction = model.predict(features)

        return jsonify({"prediction": prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the app inside Docker
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)