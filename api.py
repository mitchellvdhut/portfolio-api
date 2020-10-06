from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

projects = [
    {
        "index": 1,
        "title": "Project 1",
        "previewtext": "Lorum ipsum dolor sit amet, consectetur adipiscing elit...",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "image": "/assets/250.png"
    },
    {
        "index": 2,
        "title": "Project 2",
        "previewtext": "Lorum ipsum dolor sit amet, consectetur adipiscing elit...",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "image": "/assets/250.png"
    },
    {
        "index": 3,
        "title": "Project 3",
        "previewtext": "Lorum ipsum dolor sit amet, consectetur adipiscing elit...",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "image": "/assets/250.png"
    },
    {
        "index": 4,
        "title": "Project 4",
        "previewtext": "Lorum ipsum dolor sit amet, consectetur adipiscing elit...",
        "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "image": "/assets/250.png"
    }
]


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
    
api.add_resource(Project, "/project/<string:title>")

app.run(debug=True)