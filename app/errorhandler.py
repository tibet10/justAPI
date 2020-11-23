from flask import Flask, jsonify, json, request, abort, render_template, Blueprint, Response

errors_bp = Blueprint('errors', __name__)

@errors_bp.app_errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404