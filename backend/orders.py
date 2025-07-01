from flask import Flask, jsonify, request, abort
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('service-account.json')
firebase_admin.initialize_app(cred)

def verify_token():
    auth_header = request.headers.get('Authorization')
    if not auth_header or not auth_header.startswith('Bearer '):
        abort(401, description='Missing or invalid Authorization header')

    id_token = auth_header.split('Bearer ')[1]
    try:
        decoded_token = auth.verify_id_token(id_token)
        uid = decoded_token['uid']
        # Optional: print or log UID for debugging
        print(f'Authenticated user: {uid}')
        return uid
    except Exception as e:
        print(f'Token verification failed: {e}')
        abort(401, description='Invalid token')

@app.route('/orders', methods=['GET'])
def get_orders():
    verify_token()  # ✅ Secure this endpoint
    orders = [
        {"id": 1, "product": "Laptop", "quantity": 2},
        {"id": 2, "product": "Phone", "quantity": 1},
        {"id": 3, "product": "Headphones", "quantity": 5}
    ]
    return jsonify(orders)

# Optional Root Route
@app.route('/', methods=['GET'])
def health_check():
    return "Orders Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
