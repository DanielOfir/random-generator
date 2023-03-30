FROM python:3.9

WORKDIR /app

COPY random-generator/requirements.txt .
RUN pip install -r requirements.txt

COPY random-generator/app.py .

CMD ["python", "app.py"]