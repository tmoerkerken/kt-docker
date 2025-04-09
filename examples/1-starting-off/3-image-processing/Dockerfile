FROM python:3.11-slim
RUN pip install matplotlib
COPY script.py /app/script.py
COPY test_image.jpg /app/test_image.jpg
WORKDIR /app
CMD ["python", "script.py"]