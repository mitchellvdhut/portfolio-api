from flask import request
from flask_restful import Api, Resource, reqparse
from pymongo import MongoClient
import json

# client = MongoClient("mongodb+srv://vdhut:krtipyi7@cluster0-u7wcw.azure.mongodb.net/portfolio?retryWrites=true&w=majority")
client = MongoClient("mongodb+srv://vdhut:krtipyi7@cluster0-u7wcw.azure.mongodb.net/portfolio?retryWrites=true&w=majority")
db=client.portfolio

f = open('projects.json',)
projects = json.load(f) 

class Projects(Resource):
    def get(self):
        return projects, 200

class Project(Resource):
    def get(self):
        id = request.args.get('id')
        print(id)
        for project in projects:
            if(id == project["id"]):
                return project, 200
        return "Project not found", 404

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title", required=True, help='Project title is required')
        parser.add_argument("description", required=True, help='Project description is required')
        parser.add_argument("image")
        args = parser.parse_args()

        title = args["title"]
        
        project = {
            "title": args["title"],
            "description": args["description"],
            "image": args["image"]
        }
        
        result=db.projects.insert_one(project)
        
        print('Created project {0} with id: {1}'.format(title,result.inserted_id))
        return 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("description")
        parser.add_argument("image")
        args = parser.parse_args()

        for project in projects:
            if(id == project["id"]):
                project["title"] = args["title"]
                project["description"] = args["description"]
                project["image"] = args["image"]
                return project, 200
            
        project = {
            "title": args["title"],
            "description": args["description"],
            "image": args["image"]
        }
        projects.append(project)
        return project, 201


    def delete(self):
        global projects
        projects = [project for project in projects if project["id"] != id]
        return "{} is deleted.".format(id), 200
