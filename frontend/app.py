import requests
from flask import Flask

app = Flask(__name__)

API_GATEWAY_URL = 'https://shopsphere-gateway-7z3p42zs.uc.gateway.dev'  # Replace with your actual API Gateway URL

@app.route('/')
def home():
    return """
    <h1>Welcome to ShopSphere</h1>
    <p>Browse Products and Place Orders.</p>
    <ul>
        <li><a href="/products">View Products</a></li>
        <li><a href="/orders">View Orders</a></li>
        <li><a href="/inventory">View Inventory</a></li>
        <li><a href="/order">Place Order</a></li>
    </ul>
    """

@app.route('/products')
def products():
    try:
        response = requests.get(f'https://shopsphere-gateway-7z3p42zs.uc.gateway.dev/products')
        return response.text
    except Exception as e:
        return f"Error fetching products: {str(e)}"

@app.route('/orders')
def orders():
    try:
        response = requests.get(f'https://shopsphere-gateway-7z3p42zs.uc.gateway.dev/orders')
        return response.text
    except Exception as e:
        return f"Error fetching orders: {str(e)}"

@app.route('/inventory')
def inventory():
    try:
        response = requests.get(f'https://shopsphere-gateway-7z3p42zs.uc.gateway.dev/inventory')
        return response.text
    except Exception as e:
        return f"Error fetching inventory: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
