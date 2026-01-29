"""
Uber Price Prediction Model
Trains and saves a multivariate linear regression model for rideshare price prediction
Live App: https://uber-price-prediction-webapp.onrender.com
"""

import numpy as np
import pandas as pd
import pickle
import os

# ============================================
# LOAD AND PREPARE DATA
# ============================================

def train_model():
    """Train the model and save it to a pickle file"""
    
    # Load the rideshare dataset
    df = pd.read_csv('rideshare_kaggle.csv')
    
    # Remove rows with NaN in price (target)
    df_clean = df.dropna(subset=['price', 'distance', 'surge_multiplier'])
    
    # Select numeric features
    numeric_features = ['distance', 'surge_multiplier']
    X_numeric = df_clean[numeric_features].values
    y_train = df_clean['price'].values
    
    # Remove any remaining NaN rows
    mask = ~np.any(np.isnan(X_numeric), axis=1) & ~np.isnan(y_train)
    X_numeric = X_numeric[mask]
    y_train = y_train[mask]
    df_clean = df_clean[mask].reset_index(drop=True)
    
    # ============================================
    # One-hot encode categorical features
    # ============================================
    
    # Get unique values for cab_type and name (ride type)
    cab_types = df_clean['cab_type'].unique()
    ride_names = df_clean['name'].unique()
    
    # One-hot encode cab_type
    cab_type_encoded = pd.get_dummies(df_clean['cab_type'], prefix='cab')
    # One-hot encode ride name
    name_encoded = pd.get_dummies(df_clean['name'], prefix='ride')
    
    # ============================================
    # Z-score normalize numeric features
    # ============================================
    
    feature_means = X_numeric.mean(axis=0)
    feature_stds = X_numeric.std(axis=0)
    X_normalized = (X_numeric - feature_means) / feature_stds
    
    # ============================================
    # Build enhanced feature matrix
    # ============================================
    
    distance_norm = X_normalized[:, 0]
    surge_norm = X_normalized[:, 1]
    
    # Polynomial features
    poly_features = np.column_stack([
        distance_norm ** 2,               # distance^2
        surge_norm ** 2,                  # surge^2
        distance_norm * surge_norm,       # distance × surge interaction
    ])
    
    # Combine all features
    X_train = np.column_stack([
        X_normalized,                     # distance, surge (normalized)
        poly_features,                    # polynomial terms
        cab_type_encoded.values,          # cab type one-hot
        name_encoded.values,              # ride name one-hot
    ])
    
    # Create feature names
    enhanced_feature_names = (
        numeric_features + 
        ['distance²', 'surge²', 'distance×surge'] +
        list(cab_type_encoded.columns) +
        list(name_encoded.columns)
    )
    
    n = X_train.shape[1]
    m = X_train.shape[0]
    
    print(f"Training data shape: {X_train.shape}")
    print(f"Features: {enhanced_feature_names}")
    
    # ============================================
    # TRAIN MODEL WITH GRADIENT DESCENT
    # ============================================
    
    def compute_cost(X, y, w, b, lambda_=1):
        m = X.shape[0]
        f_wb = np.dot(X, w) + b
        errors = f_wb - y
        cost = np.dot(errors, errors) / (2 * m)
        reg_cost = (lambda_ / (2 * m)) * np.dot(w, w)
        total_cost = cost + reg_cost
        return total_cost
    
    def compute_gradient(X, y, w, b, lambda_=1):
        m, n = X.shape
        f_wb = np.dot(X, w) + b
        errors = f_wb - y
        dj_dw = np.dot(X.T, errors) / m
        dj_db = np.sum(errors) / m
        dj_dw = dj_dw + (lambda_ / m) * w
        return dj_dw, dj_db
    
    def gradient_descent(X, y, w_init, b_init, alpha, num_iters, lambda_=1):
        w = np.copy(w_init)
        b = b_init
        J_history = []
        
        for i in range(num_iters):
            dj_dw, dj_db = compute_gradient(X, y, w, b, lambda_)
            w = w - alpha * dj_dw
            b = b - alpha * dj_db
            
            if i % 100 == 0:
                cost = compute_cost(X, y, w, b, lambda_)
                J_history.append(cost)
                if i % 1000 == 0:
                    print(f"Iteration {i}: Cost = {cost:.4f}")
        
        return w, b, J_history
    
    # Initialize and train
    w_init = np.zeros(n)
    b_init = 0.0
    alpha = 0.001
    num_iters = 10000
    lambda_ = 0.01
    
    print("\nTraining model with gradient descent...")
    w_final, b_final, J_history = gradient_descent(X_train, y_train, w_init, b_init, alpha, num_iters, lambda_)
    
    print(f"Training complete! Final cost: {J_history[-1]:.4f}")
    
    # ============================================
    # SAVE MODEL AND METADATA
    # ============================================
    
    model_data = {
        'w': w_final,
        'b': b_final,
        'feature_means': feature_means,
        'feature_stds': feature_stds,
        'cab_columns': list(cab_type_encoded.columns),
        'name_columns': list(name_encoded.columns),
        'feature_names': enhanced_feature_names
    }
    
    with open('model.pkl', 'wb') as f:
        pickle.dump(model_data, f)
    
    print("Model saved to model.pkl")
    
    return model_data


def load_model():
    """Load the trained model"""
    if not os.path.exists('model.pkl'):
        print("Model not found, training new model...")
        return train_model()
    
    with open('model.pkl', 'rb') as f:
        model_data = pickle.load(f)
    
    return model_data


def predict_price(distance, surge_multiplier, cab_type, ride_name):
    """
    Make a price prediction
    
    Args:
        distance (float): Distance in miles
        surge_multiplier (float): Surge multiplier (1.0 = no surge)
        cab_type (str): Type of cab (e.g., 'Uber', 'Lyft')
        ride_name (str): Ride type (e.g., 'UberX', 'Lyft')
    
    Returns:
        float: Predicted price in dollars
    """
    model = load_model()
    
    w = model['w']
    b = model['b']
    feature_means = model['feature_means']
    feature_stds = model['feature_stds']
    cab_columns = model['cab_columns']
    name_columns = model['name_columns']
    
    # Normalize numeric features
    dist_norm = (distance - feature_means[0]) / feature_stds[0]
    surge_norm = (surge_multiplier - feature_means[1]) / feature_stds[1]
    
    # Polynomial features
    poly = np.array([dist_norm**2, surge_norm**2, dist_norm * surge_norm])
    
    # One-hot encode cab_type
    cab_onehot = np.array([1 if f'cab_{cab_type}' == col else 0 for col in cab_columns])
    
    # One-hot encode ride_name
    name_onehot = np.array([1 if f'ride_{ride_name}' == col else 0 for col in name_columns])
    
    # Build feature vector
    features = np.concatenate([[dist_norm, surge_norm], poly, cab_onehot, name_onehot])
    
    # Make prediction
    prediction = np.dot(features, w) + b
    
    # Ensure prediction is positive
    return max(0, prediction)


if __name__ == '__main__':
    # Train the model when script is run directly
    train_model()
    
    # Test predictions
    print("\n" + "="*50)
    print("Testing model predictions:")
    print("="*50)
    
    test_cases = [
        (1.0, 1.0, 'Uber', 'UberX'),
        (5.0, 1.5, 'Uber', 'UberXL'),
        (3.0, 2.0, 'Lyft', 'Lyft'),
    ]
    
    for distance, surge, cab, ride in test_cases:
        price = predict_price(distance, surge, cab, ride)
        print(f"{distance} mi, {surge}x surge, {cab} {ride}: ${price:.2f}")
