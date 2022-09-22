from flask import Flask
app = Flask(__name__)

@app.route('/') # decorator to route the request to the function
def home():
    return "Hello, World!"
