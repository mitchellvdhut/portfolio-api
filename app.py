from dotenv import load_dotenv
from flask import Flask, request
from project import get_projects, get_database, get_project, post_project, put_project, delete_project
import sys, os

if len(sys.argv) > 1:
    var_value = sys.argv[1]
else:
    var_value = 'development'

os.environ['FLASK_ENV'] = var_value

load_dotenv('.env')
app = Flask(__name__)
app.config.from_pyfile('settings.py')

projects = get_database(app)

@app.route('/projects')
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
    return 'strange error man'


print(os.environ.get('FLASK_ENV'))
if __name__ == "__main__":
    if ( os.environ.get('FLASK_ENV') == 'production' ):
        app.run(host='0.0.0.0')
    else:
        app.run()
