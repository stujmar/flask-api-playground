from flask import Flask, request
from flask_restful import Api, Resource, reqparse

# Wrap our app in an API?
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

videos = {1: {"name": "Tim", "views": 10000, "likes": 10}}

# Define a resource
class Video(Resource):
    # CREATE
    def post(self):
        pass
    # READ
    def get(self, video_id):
        print("GETTING VIDEO ID:", video_id)
        print(video_id)
        return videos[video_id]
    # UPDATE
    def put(self, video_id):
        print("PUTTING VIDEO ID:", video_id)
        args = video_put_args.parse_args()
        print(request.form)
        print(request.form["likes"])
    # DELETE
    def delete(self, video_id):
        pass

        # Add the video to the videos dictionary
        videos[video_id] = args
        
        return {video_id: args}, 201

# Add the resource to the API as an endpoint.
api.add_resource(Video, "/video/<int:video_id>")

# Check that this is the entry point.
if __name__ == '__main__':
    print("... Starting API ...")
    # Run the app. don't use debug mode in production.
    app.run(debug=True)


