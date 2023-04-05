import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def generate_random():
    # Generate a random number between 1 and 100
    num = random.randint(1, 100)

    # Send a POST request to the second microservice with the random number
    square_res = requests.post('http://manipulator-stage:80/square', json={'num': num})
    double_res = requests.post('http://manipulator-stage:80/double', json={'num': num})

    # Get the result from the second microservice
    square = square_res.json()['square']
    double = double_res.json()['double']

    return render_template('index.html', num=num, square=square, double=double)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')