from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = [
        {"id": 1, "product": "Laptop", "quantity": 2},
        {"id": 2, "product": "Phone", "quantity": 1},
        {"id": 3, "product": "Headphones", "quantity": 5}
    ]
    return jsonify(orders)

# Optional Root Route
@app.route('/', methods=['GET'])
def home():
    return "Orders Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
