"""
Flask web application for Uber Price Predictor
"""

from flask import Flask, render_template, request, jsonify
from model import predict_price, train_model
import os

app = Flask(__name__)

# Train model on startup if it doesn't exist
if not os.path.exists('model.pkl'):
    print("Training model on startup...")
    train_model()


@app.route('/')
def index():
    """Render the main prediction page"""
    return render_template('index.html')


@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for price predictions"""
    try:
        data = request.json
        
        distance = float(data.get('distance', 0))
        surge_multiplier = float(data.get('surge_multiplier', 1.0))
        cab_type = data.get('cab_type', 'Uber')
        ride_name = data.get('ride_name', 'UberX')
        
        # Validate inputs
        if distance <= 0:
            return jsonify({'error': 'Distance must be positive'}), 400
        if surge_multiplier < 1.0:
            return jsonify({'error': 'Surge multiplier must be >= 1.0'}), 400
        
        # Make prediction
        predicted_price = predict_price(distance, surge_multiplier, cab_type, ride_name)
        
        return jsonify({
            'success': True,
            'predicted_price': round(predicted_price, 2),
            'distance': distance,
            'surge_multiplier': surge_multiplier,
            'cab_type': cab_type,
            'ride_name': ride_name
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    """Health check endpoint for deployment"""
    return jsonify({'status': 'healthy'}), 200


if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
