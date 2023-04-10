import requests
from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def generate_random():

    possible_manipulations = ['square', 'double', 'triple']
    random_numbers = []
    for manipulation in possible_manipulations:
        # Send a POST request to the second microservice with the random number
        num = random.randint(1, 1000)
        random_numbers.append(num)
    res = requests.post('http://manipulator-stage:80/manipulator', json={'nums': random_numbers})
    outcome = res.json()[manipulation]

    return render_template('index.html', nums=outcome)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')