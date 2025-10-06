# server_vector.py
from flask import Flask, request, jsonify
from vector_clock import VectorClock

app = Flask(__name__)
server_clock = VectorClock("Server")

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    client_clock = data.get('vector_clock', {})

    # Merge client’s vector clock
    server_clock.update(client_clock)
    # Increment for local event
    server_clock.increment()

    result = x + y
    return jsonify({
        "result": result,
        "vector_clock": server_clock.get_clock()
    })


@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    x = data.get('x')
    y = data.get('y')
    client_clock = data.get('vector_clock', {})

    server_clock.update(client_clock)
    server_clock.increment()

    result = x * y
    return jsonify({
        "result": result,
        "vector_clock": server_clock.get_clock()
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
