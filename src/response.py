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
