# Car Price Prediction Using Machine Learning

## Project Overview
This project predicts the price of used cars using machine learning. The model is trained on a dataset containing various car attributes such as brand, model, year, engine size, fuel type, transmission type, mileage, and ownership history. The goal is to provide an objective, data-driven approach to car price estimation.

## Tech Stack Used
- **Programming Language**: Python
- **Machine Learning**: Scikit-learn, Gradient Boosting Regressor
- **Web Framework**: Flask
- **Deployment**: Docker, Heroku, AWS SageMaker, Kubernetes
- **CI/CD**: GitHub Actions
- **Cloud Storage & Registry**: Amazon Elastic Container Registry (ECR)

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/iblanco10/Car-Price-Prediction.git
cd car-price-predictor
```

### 2. Create a Virtual Environment 
```bash
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application Locally
```bash
python app.py
```
The application will be accessible at http://127.0.0.1:5000/.

## Usage Instructions
1. Open the web interface.
2. Enter car details such as brand, year, engine size, mileage, and other features.
3. Click "Predict Price" to get the estimated price.

## Deployment Information

### 1. Docker Deployment
To build and run the application in Docker:
```bash
docker build -t car-price-predictor .
docker run -p 5000:5000 car-price-predictor
```
The application will be available at http://localhost:5000/.

### 2. Heroku Deployment
The application is deployed on Heroku and accessible at:
[https://car-price-ml-f28bbeb8d2a8.herokuapp.com](https://car-price-ml-f28bbeb8d2a8.herokuapp.com)

### 3. AWS SageMaker Status
- The Docker image was successfully pushed to Amazon ECR (car-price-predictor repository in us-east-2 region).
- Issue Encountered: Deployment was not completed due to a Docker format incompatibility (OCI format vs. SageMaker required Manifest V2 Schema 2).
- Future Fix: Rebuild with DOCKER_BUILDKIT=0 or use an older Docker version.

### 4. Kubernetes Deployment
The application was deployed using Kubernetes for scalability.
- Files used: deployment.yaml and service.yaml
- Kubernetes Features: Multiple pods, automatic scaling, and load balancing.

## Model Performance & Features
- Algorithm Used: Gradient Boosting Regressor
- Performance Metrics:
  - R² Score: 0.995
  - Mean Absolute Error (MAE): 175.40
- Feature Engineering: One-hot encoding, log transformation for skewed data
- Final Model Stored as: car_price_model.pkl



