# web/app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from the Monopoly Web Dashboard!"

if __name__ == '__main__':
    # Listen on all interfaces, port 8000
    app.run(host='0.0.0.0', port=8000)