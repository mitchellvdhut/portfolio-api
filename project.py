from flask_restful import Api, Resource, reqparse
import json

f = open('projects.json',)
projects = json.load(f) 

class Projects(Resource):
    def get(self):
        return projects, 200

class Project(Resource):
    def get(self, title):
        for project in projects:
            if(title == project["title"]):
                return project, 200
        return "Project not found", 404

    def post(self, title):
        parser = reqparse.RequestParser()
        parser.add_argument("body")
        parser.add_argument("image")
        args = parser.parse_args()

        for project in projects:
            if(title == project["title"]):
                return "Project with title {} already exists".format(title), 400
            
        project = {
            "title": title,
            "body": args["body"],
            "image": args["image"]
        }
        projects.append(project)
        return project, 201

    def put(self, title):
        parser = reqparse.RequestParser()
        parser.add_argument("body")
        parser.add_argument("image")
        args = parser.parse_args()

        for project in projects:
            if(title == project["title"]):
                project["body"] = args["body"]
                project["image"] = args["image"]
                return project, 200
            
        project = {
            "title": title,
            "body": args["body"],
            "image": args["image"]
        }
        projects.append(project)
        return project, 201


    def delete(self, title):
        global projects
        projects = [project for project in projects if project["title"] != title]
        return "{} is deleted.".format(title), 200
