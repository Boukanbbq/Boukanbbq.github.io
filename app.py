from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow CORS for all routes and origins

@app.route('/order', methods=['POST'])
def handle_order():
    try:
        order_data = request.get_json()  # Get the JSON data from the request
        
        if not order_data:
            return jsonify({'error': 'No data provided'}), 400

        # Extract order details
        selected_items = order_data.get('selectedItems', {})
        address = order_data.get('address', '')
        phone_number = order_data.get('phone_number', '')
        latitude = order_data.get('latitude', None)
        longitude = order_data.get('longitude', None)

        # Basic validation
        if not address or not phone_number:
            return jsonify({'error': 'Address and phone number are required'}), 400

        # Here, you would process the order (e.g., save to database, etc.)
        # For demonstration purposes, we're just printing the order data
        print('Received order:')
        print('Selected items:', selected_items)
        print('Address:', address)
        print('Phone number:', phone_number)
        print('Latitude:', latitude)
        print('Longitude:', longitude)

        # Respond with success message
        return jsonify({'message': 'Order submitted successfully!'}), 200

    except Exception as e:
        print(f"Error handling order: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
