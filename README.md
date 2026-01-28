# Uber Price Predictor 🚗

A machine learning web application that predicts Uber/Lyft ride prices using multivariate linear regression.

## Features

- 🤖 Trained multivariate linear regression model
- 🎨 Clean and intuitive web interface
- ⚡ Real-time price predictions
- 🌐 Deployed on Render (live URL)
- 📱 Fully responsive design

## Local Setup

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/uber_price_predict.git
cd uber_price_predict
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Train the model (if needed):
```bash
python model.py
```

4. Run the Flask app:
```bash
python app.py
```

5. Open your browser and visit:
```
http://localhost:5000
```

## Usage

1. Enter the trip distance in miles
2. Specify the surge multiplier (1.0 = no surge)
3. Select the service (Uber or Lyft)
4. Choose the ride type (UberX, UberXL, Black, etc.)
5. Click "Predict Price" to get an estimate

## Model Details

- **Algorithm**: Multivariate Linear Regression with L2 Regularization
- **Features**: 
  - Distance (normalized)
  - Surge Multiplier (normalized)
  - Polynomial features (distance², surge², distance×surge)
  - One-hot encoded categorical variables
- **Training**: Gradient Descent with 10,000 iterations
- **Dataset**: Historical rideshare data

## Deployment on Render

1. Push this repository to GitHub
2. Connect your GitHub repository to Render:
   - Go to https://render.com
   - Click "New +" → "Web Service"
   - Connect your GitHub account and select this repository
3. Configure:
   - **Build Command**: `pip install -r requirements.txt && python model.py`
   - **Start Command**: `gunicorn app:app`
   - **Python Version**: 3.11
4. Deploy and get your live URL!

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
