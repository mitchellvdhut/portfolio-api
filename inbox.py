from pymongo import MongoClient
from flask import jsonify, request, Response
from flask_restful import Resource, reqparse
# from wtforms import Form, BooleanField, StringField, PasswordField, validators
from bson import json_util, ObjectId
import json


def get_messageDB(app):
    user = app.config.get("DB_USER")
    pw = app.config.get("DB_PASSWORD")
    client = MongoClient(
        f"mongodb+srv://{user}:{pw}@cluster0-u7wcw.azure.mongodb.net/portfolio?retryWrites=true&w=majority")
    db = client.portfolio
    return db.messages

def get_messages(app, messages):
    result = json.loads(json_util.dumps(messages.find()))
    return jsonify(result)

def get_message(messages):
    """"Return message with specific messageid."""
    messageid = request.args.get('messageid')
    result = json.loads(json_util.dumps(messages.find_one({"_id": ObjectId(messageid)})))
    print(result)
    return result

def post_message(messages):
    """Insert a document into the database."""
    parser = reqparse.RequestParser()
    parser.add_argument("name", required=True, help='name is required')
    parser.add_argument("email", required=True, help='e-mail address is required')
    parser.add_argument("subject", required=True, help='message subject is required')
    parser.add_argument("body", required=True, help='message body is required')
    args = parser.parse_args()

    req = request.data
    print(req, request.form)

    
    # name = StringField('name', [validators.data_required()])
    # email = StringField('email', [validators.Length(min=4), validators.data_required()])
    # subject = StringField('subject', [validators.data_required()])
    # body = StringField('body', [validators.data_required()])

    name, email, subject, body = args.values()

    message = {
        "name": name,
        "email": email,
        "subject": subject,
        "body": body,
        "read": "False"
    }
    
    result=messages.insert_one(message)
    
    print('Message posted with id: {0}'.format(result.inserted_id))
    return Response(status=201)

def put_message(messages):
    """Edit a database entry."""
    parser = reqparse.RequestParser()
    parser.add_argument("read", required=True, help='name is required')
    args = parser.parse_args()

    messageid = args["messageid"]
    filter = {"_id": ObjectId(messageid)}
    message = { "$set": {
        "title": args["title"],
        "description": args["description"],
        "image": args["image"]
    }}
    
    messages.update_one(filter, message)
    
    print('Edited message with id: {0}'.format(messageid))
    return Response(status=201)

def delete_message(messages):
    """Delete a database entry."""
    parser = reqparse.RequestParser()
    parser.add_argument("messageid", required=True, help='message id is required')
    args = parser.parse_args()

    messageid = args["messageid"]

    messages.delete_one({"_id": ObjectId(messageid)})
    return Response("Message with id: {} is deleted.".format(messageid), status=200)
