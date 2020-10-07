from flask import Flask
from flask_restful import Api, Resource, reqparse
from project import Project, Projects

app = Flask(__name__)
api = Api(app)
api.add_resource(Projects, "/")
api.add_resource(Project, "/project/<string:title>")

app.run(debug=True)