from flask import jsonify

def not_found_error(message="Resource not found"):
    return jsonify({
        "error": "Not Found",
        "message": message
    }), 404

def bad_request_error(message="Bad request"):
    return jsonify({
        "error": "Bad Request",
        "message": message
    }), 400

def server_error(message="Internal server error"):
    return jsonify({
        "error": "Server Error",
        "message": message
    }), 500