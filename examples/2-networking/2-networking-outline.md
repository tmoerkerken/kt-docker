### Incremental Example: Simulated Microscope Server & Client

**Step 1: Create a microscope TCP server**
`microscope_server.py`
```python
import socket

HOST = '0.0.0.0'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Microscope server listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(b"Simulated microscope data stream")
```

`Dockerfile`:
```Dockerfile
FROM python:3.11-slim
COPY microscope_server.py /app/microscope_server.py
WORKDIR /app
CMD ["python", "microscope_server.py"]
```

Build and run the container:
```bash
docker build -t microscope-server .
docker network create microscope-net

docker run -d --name microscope-server --network microscope-net -p 5001:5000 microscope-server
```

> Note: `-p 5001:5000` maps container port 5000 to host port 5001. The server listens on 5000 inside, but you access it on localhost:5001 from outside.

**Step 2: Connect from a local notebook client (VSCode)**
Notebook cell:
```python
# %%
import socket

HOST = 'localhost'  # Connect to Docker host
PORT = 5001          # Host port mapped to container port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = s.recv(1024)
    print("Received from microscope:", data.decode())
```

**Step 3: Docker Network Command Explained**
```bash
docker network create microscope-net
```
> This creates a custom user-defined bridge network. Containers on this network can communicate via container name (DNS-like resolution), and it's isolated from others unless explicitly connected.

