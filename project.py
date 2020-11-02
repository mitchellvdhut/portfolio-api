from pymongo import MongoClient
from flask import jsonify, request, Response
from flask_restful import Resource, reqparse
from bson import json_util, ObjectId
import json


def get_database(app):
    user = app.config.get("DB_USER")
    pw = app.config.get("DB_PASSWORD")
    client = MongoClient(
        f"mongodb+srv://{user}:{pw}@cluster0-u7wcw.azure.mongodb.net/portfolio?retryWrites=true&w=majority")
    db = client.portfolio
    return db.projects

def get_projects(app, projects):
    result = json.loads(json_util.dumps(projects.find()))
    return jsonify(result)

def get_project(projects):
    """"Return project with specific projectid."""
    projectid = request.args.get('projectid')
    result = json.loads(json_util.dumps(projects.find_one({"_id": ObjectId(projectid)})))
    print(result)
    return result

def post_project(projects):
    """Insert a document into the database."""
    parser = reqparse.RequestParser()
    parser.add_argument("title", required=True, help='Project title is required')
    parser.add_argument("description", required=True, help='Project description is required')
    parser.add_argument("image")
    args = parser.parse_args()

    print(args)
    title = args["title"]

    project = {
        "title": args["title"],
        "description": args["description"],
        "image": args["image"]
    }
    
    result=projects.insert_one(project)
    
    print('Created project {0} with id: {1}'.format(title,result.inserted_id))
    return Response(status=201)

def put_project(projects):
    """Edit a database entry."""
    parser = reqparse.RequestParser()
    parser.add_argument("projectid", required=True, help='Project id is required')
    parser.add_argument("title", required=True, help='Project title is required')
    parser.add_argument("description", required=True, help='Project description is required')
    parser.add_argument("image")
    args = parser.parse_args()

    projectid = args["projectid"]
    filter = {"_id": ObjectId(projectid)}
    project = { "$set": {
        "title": args["title"],
        "description": args["description"],
        "image": args["image"]
    }}
    
    projects.update_one(filter, project)
    
    print('Edited project with id: {0}'.format(projectid))
    return Response(status=201)

def delete_project(projects):
    """Delete a database entry."""
    parser = reqparse.RequestParser()
    parser.add_argument("projectid", required=True, help='Project id is required')
    args = parser.parse_args()

    projectid = args["projectid"]

    projects.delete_one({"_id": ObjectId(projectid)})
    return Response("Post with id: {} is deleted.".format(projectid), status=200)
