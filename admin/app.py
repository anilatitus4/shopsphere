import os
from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, auth

app = Flask(__name__, template_folder='templates')

# Initialize Firebase Admin SDK (download serviceAccountKey from Firebase Console)
cred = credentials.Certificate('serviceAccountKey.json')  # <-- Place the file in your admin folder
firebase_admin.initialize_app(cred)

@app.route('/')
def home():
    return "<h1>Welcome to ShopSphere Admin Portal</h1> <a href='/admin_login'>Login</a>"

@app.route('/admin_login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/verify_token', methods=['POST'])
def verify_token():
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        return 'Missing Authorization header', 401

    id_token = auth_header.split('Bearer ')[-1]

    try:
        decoded_token = auth.verify_id_token(id_token)
        user_email = decoded_token['email']
        return f'Login verified for user: {user_email}', 200
    except Exception as e:
        print(e)
        return 'Invalid token', 401

@app.route('/admin_dashboard')
def admin_dashboard():
    return "<h2>Welcome to the Admin Dashboard! You are authenticated.</h2>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
