### Example: Simulated Microscope + Client via Compose

**Step 1: server1/server1.py**
```python
import socket

HOST = '0.0.0.0'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server 1 listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(b"Simulated data from Server 1")

```

**Step 2: server2/server2.py**
```python
import socket

HOST = '0.0.0.0'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server 1 listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        conn.sendall(b"Simulated data from Server 1")

```

**Step 3: Folder structure**
```
./3-compose/
├── docker-compose.yml
├── server1/
│   ├── Dockerfile
│   └── server1.py
├── server2/
│   ├── Dockerfile
│   └── server2.py
└── notebook.py

```

**server1/Dockerfile**
```Dockerfile
FROM python:3.11-slim
COPY server1.py /app/
WORKDIR /app
CMD ["python", "server1.py"]
```

**server2/Dockerfile**
```Dockerfile
FROM python:3.11-slim
COPY server2.py /app/
WORKDIR /app
CMD ["python", "server2.py"]
```

**docker-compose.yml**
```yaml
version: '3.9'
services:
  server1:
    build: ./server1
    ports:
      - "5000:5000"  # Expose port 5000 on localhost

  server2:
    build: ./server2
    ports:
      - "6000:6000"  # Expose port 6000 on localhost
```

**Step 4: Run the servers**
```bash
docker-compose up --build
```

**Output:**
Run the notebook cells!

**Recap:**
- Docker Compose simplifies networking and container startup order.
- Compose mirrors real-world setups where clients connect to services by name.
- The YAML format is easy to read