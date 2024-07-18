from flask import jsonify
from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt


def admin_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request() # Raise Exception if invalid JWT is in the request
        claims = get_jwt()
        if claims['roles'] != "admin":
            return jsonify({
                "body": {
                    "error": "Access denied",
                    "message": "You do not have permission to access this resource. Only administrators can perform this operation."
                },
                "status_code": 403,
            })
        else:
            return function(**args, **kwargs)
    
    return wrapper
        
