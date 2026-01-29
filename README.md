# Uber Price Predictor 🚗

**Live App**: https://uber-price-prediction-webapp.onrender.com

A machine learning web application that predicts Uber/Lyft ride prices using multivariate linear regression.

## Features

- 🤖 Trained multivariate linear regression model
- 🎨 Clean and intuitive web interface
- ⚡ Real-time price predictions
- 🌐 Live on Render
- 📱 Fully responsive design

## Usage

1. Visit the live app above
2. Enter the trip distance in miles
3. Specify the surge multiplier (1.0 = no surge)
4. Select the service (Uber or Lyft)
5. Choose the ride type (UberX, UberXL, Black, etc.)
6. Click "Predict Price" to get an estimate

## Model Details

- **Algorithm**: Multivariate Linear Regression with L2 Regularization
- **Features**: 
  - Distance (normalized)
  - Surge Multiplier (normalized)
  - Polynomial features (distance², surge², distance×surge)
  - One-hot encoded categorical variables
- **Training**: Gradient Descent with 10,000 iterations
- **Dataset**: Historical rideshare data

## File Structure

```
├── app.py                 # Flask application
├── model.py               # ML model training and inference
├── model.pkl              # Trained model (generated on first run)
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku/Render deployment config
├── runtime.txt            # Python version specification
├── render.yaml            # Render-specific configuration
├── rideshare_kaggle.csv   # Training dataset
└── templates/
    └── index.html         # Web interface
```

## API Endpoints

### POST `/api/predict`
Predicts the price for a ride.

**Request Body:**
```json
{
  "distance": 2.5,
  "surge_multiplier": 1.5,
  "cab_type": "Uber",
  "ride_name": "UberX"
}
```

**Response:**
```json
{
  "success": true,
  "predicted_price": 12.50,
  "distance": 2.5,
  "surge_multiplier": 1.5,
  "cab_type": "Uber",
  "ride_name": "UberX"
}
```

### GET `/health`
Health check endpoint for deployment monitoring.

## Technologies

- **Backend**: Flask, NumPy, Pandas
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Render, GitHub
- **ML**: Gradient Descent, Linear Regression
