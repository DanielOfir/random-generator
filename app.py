import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def generate_random():
    # Generate a random number between 1 and 100
    num = random.randint(1, 100)

    # Send a POST request to the second microservice with the random number
    res = requests.post('http://manipulator-stage:80/manipulator', json={'num': num})

    # Get the result from the second microservice
    square = res.json()['square']
    double = res.json()['double']
    triple = res.json()['triple']

    return render_template('index.html', num=num, square=square, double=double, triple=triple)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')