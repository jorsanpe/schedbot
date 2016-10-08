# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, abort, make_response, send_from_directory
from flask.ext.login import LoginManager
from add_task import AddTask
from task_repository_mongo import TaskRepositoryMongo
from user_repository_mongo import UserRepositoryMongo
import os

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

if not os.environ.has_key('OPENSHIFT_DATA_DIR'):
    os.environ['OPENSHIFT_DATA_DIR'] = os.path.dirname(os.path.abspath(__file__))


@app.route('/task-list')
def event_form():
    return process(Request(Type='event_form'))


@app.route('/add-task', methods=['POST'])
def submit_event():
    try:
        data = dict((key, request.form[key]) for key in request.form.keys())
        add_task = AddTask()
        user_repo = UserRepositoryMongo()
        return add_task()
    except:
        return make_response(jsonify({'error': 'Could not submit event'}), 400)


@app.route('/')
def index():
    return process(Request(Type='event_list'))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    pass
