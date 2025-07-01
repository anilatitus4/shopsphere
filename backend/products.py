from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Phone", "price": 400},
        {"id": 3, "name": "Headphones", "price": 50}
    ]
    return jsonify(products)

# Optional Root Route
@app.route('/', methods=['GET'])
def home():
    return "Products Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
