from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

# Wrap our app in an API?
app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

videos = {1: {"name": "Tim", "views": 10000, "likes": 10}}

# Is this a custom exception?
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")

# Define a resource
class Video(Resource):

    # CREATE
    def post(self, video_id):
        args = video_put_args.parse_args()
        if video_id in videos.keys():
            return {video_id: args}, 409
        videos[video_id] = args
        return {video_id: args}, 201

    # READ
    def get(self, video_id):
        abort_if_video_id_doesnt_exist(video_id)
        return videos[video_id], 200

    # UPDATE
    def put(self, video_id):
        args = video_put_args.parse_args()
        if video_id not in videos.keys():
            videos[video_id] = args
            return {video_id: args}, 201
        else:
            videos[video_id] = args
            return {video_id: args}, 200

    # DELETE
    def delete(self, video_id):
        # remove video from videos
        del videos[video_id]
        return None, 204


# Add the resource to the API as an endpoint.
api.add_resource(Video, "/video/<int:video_id>")

# Check that this is the entry point.
if __name__ == "__main__":
    print("... Starting API ...")
    # Run the app. don't use debug mode in production.
    app.run(debug=True)


