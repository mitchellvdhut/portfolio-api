from flask import request
from flask_restful import Api, Resource, reqparse
import json

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
        parser.add_argument("title")
        parser.add_argument("body")
        parser.add_argument("image")
        args = parser.parse_args()

        for project in projects:
            if(id == project["id"]):
                return "Project with title {} already exists".format(id), 400
            
        project = {
            "title": args["title"],
            "body": args["body"],
            "image": args["image"]
        }
        projects.append(project)
        return project, 201

    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("title")
        parser.add_argument("body")
        parser.add_argument("image")
        args = parser.parse_args()

        for project in projects:
            if(id == project["id"]):
                project["title"] = args["title"]
                project["body"] = args["body"]
                project["image"] = args["image"]
                return project, 200
            
        project = {
            "title": args["title"],
            "body": args["body"],
            "image": args["image"]
        }
        projects.append(project)
        return project, 201


    def delete(self):
        global projects
        projects = [project for project in projects if project["id"] != id]
        return "{} is deleted.".format(id), 200
