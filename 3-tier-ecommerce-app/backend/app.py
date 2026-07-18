from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {
        "id":1,
        "name":"Laptop",
        "price":55000
    },
    {
        "id":2,
        "name":"Mobile",
        "price":25000
    },
    {
        "id":3,
        "name":"Headphones",
        "price":3000
    }
]

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/")
def home():
    return "Backend Running Successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
