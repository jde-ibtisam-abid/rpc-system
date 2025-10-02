# server.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    x, y = data["x"], data["y"]
    return jsonify({"result": x + y})

@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    x, y = data["x"], data["y"]
    return jsonify({"result": x * y})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
