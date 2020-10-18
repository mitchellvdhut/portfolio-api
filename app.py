from dotenv import load_dotenv
from flask import Flask
from project import get_projects

load_dotenv('.env')
app = Flask(__name__)
app.config.from_pyfile('settings.py')


@app.route('/projects/')
def get_all_projects():
    return get_projects(app)


app.run()
