import os
import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# Verifies upload file allowed extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Renders error messages
def error(message, code=400):
    """Render error messages to the user."""
    # Enables paragraph division on messages
    message=message.split("\n")

    return render_template("error.html", message=message, code=code)


# Enables mandatory login for access to pages
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
