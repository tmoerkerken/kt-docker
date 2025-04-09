
### Incremental Example for Python + NumPy + Image Processing:

**Step 0: Base docker images**
```Dockerfile
FROM ubuntu:20.04
RUN apt-get update && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python
CMD ["python", "--version"]
```
Build and run:
```bash
docker build -f Dockerfile.ubuntu20 -t ubuntu20 .
docker run ubuntu20
```

Same manner for the other images. See how the Python version differs.

**Step 1: Minimal Python container**
```Dockerfile
FROM python:3.11-slim
COPY script.py /app/script.py
WORKDIR /app
CMD ["python", "script.py"]
```
`script.py`
```python
print("Hello from Python in Docker")
```
Build and run:
```bash
docker build -t py-minimal .
docker run py-minimal
```

**Step 2: Add NumPy and a basic operation**
```Dockerfile
FROM python:3.11-slim
RUN pip install numpy
COPY script.py /app/script.py
WORKDIR /app
CMD ["python", "script.py"]
```
`script.py`
```python
import numpy as np
print(np.arange(10))
```
```bash
docker build -t py-numpy .
docker run py-numpy
```
> Demonstrates caching: if Python version or pip install hasn't changed, the layer is reused.

**Step 3: Add image loading with matplotlib**
```Dockerfile
FROM python:3.11-slim
RUN pip install matplotlib
COPY script.py /app/script.py
COPY test_image.jpg /app/test_image.jpg
WORKDIR /app
CMD ["python", "script.py"]
```
`script.py`
```python
import matplotlib.pyplot as plt
image = plt.imread("test_image.jpg")
print("Image shape")
print(image.shape)
```
```bash
docker build -t py-imageproc .
docker run py-imageproc
```
> Now your container performs a simple image read and processing check!


**Step 4: Shared folders**
```Dockerfile
FROM python:3.11-slim

WORKDIR /app
# Create code directory
RUN mkdir /app/code

CMD ["python", "code/print.py"]
```
`print.py`
```python
print("this is shared between host and docker")
```
```bash
docker build -t python-print .
docker run -v .:/app/code python-print
```

**Step 5: reusing images**
```Dockerfile
FROM ubuntu:20.04
RUN apt-get update && \
    apt-get install -y python3 && \
    ln -s /usr/bin/python3 /usr/bin/python
CMD ["python", "--version"]

```
```Dockerfile
FROM ubuntu20-with-python
CMD ["python", "-c", "print('Hello Delmic!')"]
```

```bash
docker build -f Dockerfile.base -t ubuntu20-with-python .
docker build -f Dockerfile.inherit -t ubuntu20-inherit .
docker run ubuntu20-inherit
```

**Bonus Tips:**
- Add `--no-cache` to disable layer reuse and test full builds.
- Use `.dockerignore` to avoid copying unnecessary files.

**Commands Recap:**
- `docker build`: Build image from Dockerfile
- `docker run`: Run a container from an image
- `docker ps`: See running containers
- `docker images`: List local images
- `docker history <image>`: View image layers and caching behavior
- `docker inspect <container>`: View container configuration
- `docker exec -it <container_name_or_id> /bin/bash`: Start shell session in container