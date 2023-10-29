from flask import (
    Blueprint,
    request,
    jsonify,
    render_template,
    session
)
from functools import wraps

auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return 'Logged in currently!'


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
