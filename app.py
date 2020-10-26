from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from project import get_projects, get_database, get_project, post_project, put_project, delete_project
from inbox import get_messages, get_messageDB, get_message, post_message, put_message, delete_message
import sys, os

if len(sys.argv) > 1:
    var_value = sys.argv[1]
else:
    var_value = 'development'

os.environ['FLASK_ENV'] = var_value

load_dotenv('.env')
app = Flask(__name__)
app.config.from_pyfile('settings.py')
CORS(app)

projects = get_database(app)
messages = get_messageDB(app)

@app.route('/projects/', methods=['GET'])
def get_all_projects():
    return get_projects(app, projects)

@app.route('/project', methods=['GET', 'POST', 'PUT', 'DELETE'])
def project():
    if (request.method == 'GET'):
        return get_project(projects)
    if (request.method == 'POST'):
        return post_project(projects)
    if (request.method == 'PUT'):
        return put_project(projects)
    if (request.method == 'DELETE'):
        return delete_project(projects)
    return 'Invalid request'

# @app.route('/inbox/')
# def get_all_messages():
#     return get_messages(app, messages)

# @app.route('/inbox/message', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def message():
#     if (request.method == 'GET'):
#         return get_message(messages)
#     if (request.method == 'POST'):
#         return post_message(messages)
#     if (request.method == 'PUT'):
#         return put_message(messages)
#     if (request.method == 'DELETE'):
#         return delete_message(messages)
#     return 'Invalid request'


print(os.environ.get('FLASK_ENV'))
if __name__ == "__main__":
    if ( os.environ.get('FLASK_ENV') == 'production' ):
        app.run(host='0.0.0.0')
    else:
        app.run()
