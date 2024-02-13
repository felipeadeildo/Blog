from functools import wraps

from flask import jsonify, session


def message(message: str, status_code: int = 200, **kw):
    return jsonify({"message": message, **kw}), status_code


def login_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not session.get("user_id"):
                return message("Unauthorized", 401)
            return f(*args, **kwargs)

        return decorated_function

    return decorator
