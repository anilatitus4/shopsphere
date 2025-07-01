from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/inventory', methods=['GET'])
def get_inventory():
    inventory = [
        {"id": 1, "product": "Laptop", "stock": 15},
        {"id": 2, "product": "Phone", "stock": 30},
        {"id": 3, "product": "Headphones", "stock": 100}
    ]
    return jsonify(inventory)

# ✅ New Root Route
@app.route('/', methods=['GET'])
def home():
    return "Inventory Service Running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
