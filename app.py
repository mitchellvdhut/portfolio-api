from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
from project import Project, Projects

app = Flask(__name__)
CORS(app)
api = Api(app)
api.add_resource(Projects, "/")
api.add_resource(Project, "/project")

if __name__ == "__main__":
    app.run()