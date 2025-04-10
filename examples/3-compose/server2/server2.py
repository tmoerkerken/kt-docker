import socket

HOST = '0.0.0.0'
PORT = 6000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server 2 listening on {HOST}:{PORT}")

    while True:  # Keep the server running to accept multiple connections
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}", flush=True)
            conn.sendall(b"Simulated data from Server 2")
