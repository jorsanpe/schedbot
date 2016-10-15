# -*- coding: utf-8 -*-
# Copyright 2016 Jordi Sánchez
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

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
