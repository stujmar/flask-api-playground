from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # decorator to route the request to the function
@app.route("/index")
@app.route("/home") # Pro tip: you can chain decorators
def home():
    return "Hello, World!"

# Routes can contain methods
@app.route("/api/v1/users/", methods=["GET", "POST", "PUT", "DELETE"])
def users():
    return "Users"

# Dynamic values in routes
@app.route("/user/<username>")
def profile(username):
    return f"User: {username}"

@app.route("<int:year>/<int:month>/<title>") # possible types string, int, float, path
def article(year, month, title):
    return f"{year} - {month} - {title}"


