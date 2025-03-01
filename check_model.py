import joblib

# Load the model
model = joblib.load("car_price_model.pkl")

# Check if it has feature names (scikit-learn models might have this)
if hasattr(model, 'feature_names_in_'):
    print("Feature names:")
    print(model.feature_names_in_)
else:
    print("Model doesn't have feature_names_in_ attribute")
    
# Try to get other information about the model
print("\nModel type:", type(model))

# If it's a pipeline, we can check its steps
if hasattr(model, 'steps'):
    print("\nPipeline steps:")
    for step_name, step_estimator in model.steps:
        print(f"- {step_name}: {type(step_estimator)}")

# Check what other attributes the model has
print("\nOther potentially useful attributes:")
for attr in dir(model):
    if not attr.startswith('_') and attr not in ['feature_names_in_']:
        print(f"- {attr}")
