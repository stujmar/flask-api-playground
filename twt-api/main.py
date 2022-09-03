from flask import Flask
from flask_restful import Api, Resource

# Wrap our app in an API?
app = Flask(__name__)
api = Api(app)

# Define a resource.
class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World"}

# Add the resource to the API as an endpoint.
api.add_resource(HelloWorld, "/helloworld")

# Check that this is the entry point.
if __name__ == '__main__':
    # Run the app. don't use debug mode in production.
    app.run(debug=True)


