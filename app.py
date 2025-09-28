from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env if available
load_dotenv()

app = Flask(__name__)

# Enable CORS (allow all origins, restrict to GET requests)
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

# Define the /products endpoint
@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

if __name__ == "__main__":
    # Get PORT from env or default to 3030
    port = int(os.getenv("PORT", 3030))
    # Run server on 0.0.0.0 so it's accessible externally
    app.run(host="0.0.0.0", port=port)
