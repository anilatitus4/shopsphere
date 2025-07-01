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

@app.route('/products', methods=['GET'])
def get_products():
    verify_token()  # ✅ Secure this endpoint
    products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Phone", "price": 400},
        {"id": 3, "name": "Headphones", "price": 50}
    ]
    return jsonify(products)

# Optional Root Route
@app.route('/', methods=['GET'])
def health_check():
    return "Products Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
