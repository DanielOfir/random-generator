import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def generate_random():

    # Send a POST request to the second microservice with the random number
    num = random.randint(1, 1000)
    res = requests.post('http://manipulator-stage:80/manipulator', json={'num': num})
    outcome = res.json()

    return render_template('index.html', num=outcome)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')