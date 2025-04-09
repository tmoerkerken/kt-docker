FROM python:3.11-slim
RUN apt-get update && apt-get install -y xvfb && \
    pip install pyvirtualdisplay matplotlib
COPY render.py /app/render.py
WORKDIR /app
CMD ["python", "render.py"]