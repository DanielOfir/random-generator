import requests
from flask import Flask
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

    html = '''
    <html>
        <head>
            <style>
                body {{
                    background-color: darkcyan;
                }}
            </style>
            <title>Random Number Manipulator</title>
        </head>
        <body>
            <h1 style="text-align:center">Random Number Manipulator</h1>
            <p style="text-align:center">
                The square of {} is {}.<br>
                And the double of {} is {}.
            </p>
        </body>
    </html>
    '''

    # Return the original number and its square
    return html.format(num, square, num, double)

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')