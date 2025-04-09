
### Example: Running GUI or Screenshot-Capture Apps in Docker

### GUI window
To run a full GUI app inside Docker (like a Python wx or Qt app):
a fully working example of the **`my-gui-app`** setup that runs a simple **wxPython GUI window** inside a Docker container on a Linux host using X11 forwarding.

---

##### 🐍 `main.py` – A simple GUI app using wxPython

```python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello from wxPython in Docker")
panel = wx.Panel(frame)
text = wx.StaticText(panel, label="This is a GUI running in Docker!", pos=(10, 10))
frame.Show(True)
app.MainLoop()
```

---

##### 🐳 `Dockerfile` – GUI-capable wxPython environment

```Dockerfile
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    x11-apps \
    libgtk-3-0 \
    libgl1-mesa-glx \
    libx11-xcb1 \
    && rm -rf /var/lib/apt/lists/*

# Install wxPython
RUN pip install wxPython

# Copy app
COPY main.py /app/main.py
WORKDIR /app

CMD ["python", "main.py"]
```

---

##### 🧪 Build and Run Instructions (Linux Host with X11)

1. **Allow Docker access to X11:**

```bash
xhost +local:docker
```

2. **Build the Docker image:**

```bash
docker build -t my-gui-app .
```

3. **Run the container with X11 socket mounted:**

```bash
docker run --rm \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  --network host \
  my-gui-app
```

---

##### ⚠️ Requirements

- Only works on **Linux hosts** using native X11.
- For **macOS** or **Windows**, you'd need XQuartz or an X11 server with port forwarding (more complex).
- The `--network host` flag helps ensure low-latency local communication (some GUI toolkits can misbehave otherwise).


### Headless rendering
For **headless rendering** (e.g., generating images or screenshots):
  - Use lightweight alternatives like [pyvirtualdisplay](https://pypi.org/project/pyvirtualdisplay/) and `Xvfb`:

  `Dockerfile`:
  ```Dockerfile
  FROM python:3.11-slim
  RUN apt-get update && apt-get install -y xvfb && \
      pip install pyvirtualdisplay matplotlib
  COPY render.py /app/render.py
  WORKDIR /app
  CMD ["python", "render.py"]
  ```

  `render.py`:
  ```python
  from pyvirtualdisplay import Display
  import matplotlib.pyplot as plt

  Display().start()
  plt.plot([0, 1, 2], [0, 1, 4])
  plt.savefig("plot.png")
  ```

  ```
  docker run -it headless-render /bin/sh
  ```

  or (adjust for this file)

  ```
  docker cp headless-render:/app/output/plot.png ./docker-output/
  ```
- This keeps the container light and avoids needing a full desktop GUI.

### Shared folder
For **headless rendering** (e.g., generating images or screenshots):
  - Use lightweight alternatives like [pyvirtualdisplay](https://pypi.org/project/pyvirtualdisplay/) and `Xvfb`:

  `Dockerfile`:
  ```Dockerfile
  FROM python:3.11-slim

  RUN apt-get update && apt-get install -y xvfb && \
      pip install pyvirtualdisplay matplotlib

  COPY render.py /app/render.py
  WORKDIR /app

  # Create output directory
  RUN mkdir /app/output

  CMD ["python", "render.py"]
  ```

  `render.py`:
  ```python
  from pyvirtualdisplay import Display
  import matplotlib.pyplot as plt

  Display().start()
  plt.plot([0, 1, 2], [0, 1, 4])
  plt.savefig("/app/output/plot.png")
  ```
  Now run:

  ```bash
  mkdir -p ./docker-output  # create host output directory
  docker run --rm -v ./docker-output:/app/output shared-folder-app
  ```

  Debug with:
  ```bash
  docker run --rm -it -v ./docker-output:/app/output headless-render python -m pdb render.py
  ```

**Summary:**
- Docker is not ideal for interactive GUIs, but with tricks like X11, VNC, or headless rendering, it's often possible.
- For GUI-heavy workflows, VMs may still be the better choice.
- But for **automated rendering**, screenshots, or simple plotting, Docker can stay lightweight and effective.
