from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    return jsonify({"result": data["x"] + data["y"]})

@app.route("/multiply", methods=["POST"])
def multiply():
    data = request.get_json()
    return jsonify({"result": data["x"] * data["y"]})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))   # 👈 use Railway’s PORT
    app.run(host="0.0.0.0", port=port)         # 👈 important
