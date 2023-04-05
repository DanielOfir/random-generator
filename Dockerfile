FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY templates/ templates/

RUN pip install -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]

# COPY web directory to .

