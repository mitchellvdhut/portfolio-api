from pymongo import MongoClient
from flask import jsonify
from bson import json_util
import json


def get_database(app):
    user = app.config.get("DB_USER")
    pw = app.config.get("DB_PASSWORD")
    client = MongoClient(
        f"mongodb+srv://{user}:{pw}@cluster0-u7wcw.azure.mongodb.net/portfolio?retryWrites=true&w=majority")
    db = client.portfolio
    return db.projects


def get_projects(app):
    projects = get_database(app)
    result = json.loads(json_util.dumps(projects.find()))
    return jsonify(result)

