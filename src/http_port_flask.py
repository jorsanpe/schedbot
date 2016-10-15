# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, make_response
from flask.ext.login import LoginManager
from add_task import AddTask
from schedbot_config import user_repo, task_repo

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@app.route('/submit-task', methods=['POST'])
def submit_task():
    try:
        data = dict((key, request.form[key]) for key in request.form.keys())
        add_task = AddTask(user_repo(), task_repo())
        return add_task()
    except:
        return make_response(jsonify({'error': 'Could not submit task'}), 400)


@app.route('/')
def index():
    return '{}'


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    pass
