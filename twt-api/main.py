from os.path import exists
from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

# Wrap our app in an API?
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False) # has to have some info, nullable=True means it can be empty
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"

if not exists("database.db"):
    db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required", required=True)

videos = {1: {"name": "Tim", "views": 10000, "likes": 10}}

# Is this a custom exception?
def abort_if_video_id_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Could not find video...")

def abort_if_exists(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID...")

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
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            return result, 200
        else:
            return None, 404
        # Old non db code
        # abort_if_video_id_doesnt_exist(video_id)
        # return videos[video_id], 200

    # UPDATE
    def put(self, video_id):
        args = video_put_args.parse_args()
        abort_if_exists(video_id)
        if video_id not in videos.keys():
            videos[video_id] = args
            return {video_id: args}, 201
        # else:
        #     videos[video_id] = args
        #     return {video_id: args}, 200

    # DELETE
    def delete(self, video_id):
        # remove video from videos
        abort_if_video_id_doesnt_exist(video_id)
        del videos[video_id]
        return None, 204 # could be empty string instead of None


# Add the resource to the API as an endpoint.
api.add_resource(Video, "/video/<int:video_id>")

# Add a route to the API for templating.
@app.route("/")
def home():
    return render_template("index.html")

# Check that this is the entry point.
if __name__ == "__main__":
    print("... Starting API ...")
    # Run the app. don't use debug mode in production.
    app.run(debug=True)


