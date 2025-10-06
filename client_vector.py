import requests
import time
import random
from vector_clock import VectorClock

SERVER_URL = "http://localhost:8080"
CLIENT_ID = "ClientA"  # change to "ClientB" for the second client

# Initialize local vector clock
client_clock = VectorClock(CLIENT_ID)
print(f"Initial vector clock: {client_clock.clock}\n")

def rpc_call(operation, x, y):
    """Send RPC request with vector clock propagation."""
    # Step 1 – increment before sending
    client_clock.increment()

    payload = {
        "x": x,
        "y": y,
        "vector_clock": client_clock.clock
    }

    # Step 2 – send the request
    response = requests.post(f"{SERVER_URL}/{operation}", json=payload)
    data = response.json()

    # Step 3 – merge server’s clock
    if "vector_clock" in data:
        client_clock.update(data["vector_clock"])

    # Step 4 – show result
    print(f"[{operation.upper()}] x={x}, y={y}")
    print(f"Result: {data.get('result')}")
    print(f"Client vector clock now: {client_clock.clock}\n")

    # Step 5 – random short delay (1–3 seconds)
    time.sleep(random.uniform(1, 3))

# --- Only 3 RPC Calls ---
operations = [
    ("add", 2, 3),
    ("multiply", 4, 5),
    ("add", 10, 20)
]

for op, x, y in operations:
    rpc_call(op, x, y)

print("Final client vector clock:", client_clock.clock)
