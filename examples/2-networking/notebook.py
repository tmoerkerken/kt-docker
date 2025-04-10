# %%
import socket

HOST = 'localhost'  # Connect to Docker host
PORT = 5001          # Host port mapped to container port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print("Received from microscope:", data.decode())
# %%
