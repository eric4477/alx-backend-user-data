#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from typing import Literal, Tuple

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> Tuple[str, Literal[404]]:
    """
    Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> Tuple[str, Literal[401]]:
    """
    Unauthorized access handler
    """
    return jsonify({"error": "unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> Tuple[str, Literal[403]]:
    """
    Forbidden access handler
    """
    return jsonify({"error": "forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=int(port))
