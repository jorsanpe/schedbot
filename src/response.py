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

def __fail(code):
    return {
        'status': 'fail',
        'code': str(code),
    }


def user_not_found():
    return __fail(400)


def user_created():
    return {
        'status': 'success',
        'code': 0,
    }


def user_already_exists():
    return __fail(400)


def json_with(tasks):
    return {
        'status': 'success',
        'code': '0',
        'data': [t.as_dict() for t in tasks],
    }
