from flask import Flask, render_template, make_response, redirect, url_for

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

# Flask route which returns a JSON response
@app.route("/api/v2/test_response")
def test_response():
  headers = {"Content-Type": "application/json"}
  return make_response({"message": "Hello, World!"}, 200, headers)

# Dynamic values in routes
@app.route("/user/<username>")
def profile(username):
    return f"User: {username}"

@app.route("/date/<int:year>/<int:month>/<title>") # possible types string, int, float, path
def article(year, month, title):
    return f"{year} - {month} - {title}"

# use a render template to return a html file
@app.route("/template")
def template():
    return render_template("index.html")

# Use a route to redirect to another route
@app.route("/restricted")
def restricted():
    return redirect("/")

# Use a route to redirect to another route via a function name
@app.route("/restricted2")
def restricted2():
    return redirect(url_for("template"))

# Check that this is the entry point.
if __name__ == "__main__":
    print("... Starting API ...")
    # Run the app. don't use debug mode in production.
    app.run(debug=True)
