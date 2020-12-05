from pymongo import MongoClient
from flask import jsonify, request, Response
from flask_restful import Resource, reqparse
# from wtforms import Form, BooleanField, StringField, PasswordField, validators
from bson import json_util, ObjectId
import json


def get_postDB(app):
    user = app.config.get("DB_USER")
    pw = app.config.get("DB_PASSWORD")
    client = MongoClient(
        f"mongodb+srv://{user}:{pw}@cluster0-u7wcw.azure.mongodb.net/portfolio?retryWrites=true&w=majority")
    db = client.portfolio
    return db.posts

def get_posts(app, posts):
    result = json.loads(json_util.dumps(posts.find()))
    return jsonify(result)

def get_post(posts):
    """"Return post with specific postid."""
    postid = request.args.get('postid')
    result = json.loads(json_util.dumps(posts.find_one({"_id": ObjectId(postid)})))
    print(result)
    return result

def post_post(posts):
    """Insert a document into the database."""
    parser = reqparse.RequestParser()
    parser.add_argument("title", required=True, help='title is required')
    parser.add_argument("body", required=True, help='post content is required')
    args = parser.parse_args()

    req = request.data
    print(req, request.form)

    
    # name = StringField('name', [validators.data_required()])
    # email = StringField('email', [validators.Length(min=4), validators.data_required()])
    # subject = StringField('subject', [validators.data_required()])
    # body = StringField('body', [validators.data_required()])

    title, body = args.values()

    post = {
        "title": title,
        "body": body,
    }
    
    result=posts.insert_one(post)
    
    print('Post posted with id: {0}'.format(result.inserted_id))
    return Response(status=201)

def put_post(posts):
    """Edit a database entry."""
    parser = reqparse.RequestParser()
    parser.add_argument("read", required=True, help='name is required')
    args = parser.parse_args()

    postid = args["postid"]
    filter = {"_id": ObjectId(postid)}
    post = { "$set": {
        "title": args["title"],
        "body": args["body"]
    }}
    
    posts.update_one(filter, post)
    
    print('Edited post with id: {0}'.format(postid))
    return Response(status=201)

def delete_post(posts):
    """Delete a database entry."""
    parser = reqparse.RequestParser()
    parser.add_argument("postid", required=True, help='post id is required')
    args = parser.parse_args()

    postid = args["postid"]

    posts.delete_one({"_id": ObjectId(postid)})
    return Response("Post with id: {} is deleted.".format(postid), status=200)
