from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("car_price_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get data from the form
        make = request.form.get("make")
        year = int(request.form.get("year"))
        engine_size = float(request.form.get("engine_size"))
        mileage = int(request.form.get("mileage"))
        doors = int(request.form.get("doors"))
        owners = int(request.form.get("owners"))
        fuel_type = request.form.get("fuel_type")
        transmission = request.form.get("transmission")
        
        # Create a DataFrame with a single row
        input_data = {
            'Year': year,
            'Engine_Size': engine_size,
            'Mileage': mileage,
            'Doors': doors,
            'Owner_Count': owners,
        }
        
        # Add all categorical features initialized to 0
        for col in model.feature_names_in_:
            if col not in input_data:
                input_data[col] = 0
        
        # Set appropriate brand based on selection
        brand_key = f'Brand_{make}'
        if brand_key in input_data:
            input_data[brand_key] = 1
            
        # Set appropriate fuel type
        fuel_key = f'Fuel_Type_{fuel_type}'
        if fuel_key in input_data:
            input_data[fuel_key] = 1
            
        # Set transmission
        if transmission == "Manual":
            input_data['Transmission_Manual'] = 1
        elif transmission == "Automatic":
            input_data['Transmission_Semi-Automatic'] = 1
            
        # Create DataFrame with all the features in the right order
        df = pd.DataFrame([input_data])
        
        # Ensure columns are in the same order as expected by the model
        df = df[model.feature_names_in_]
        
        # Make prediction
        predicted_price = model.predict(df)[0]
        
        return render_template("index.html", prediction=predicted_price)
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)