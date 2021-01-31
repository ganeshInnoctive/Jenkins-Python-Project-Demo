from flask import Blueprint, jsonify, request, render_template
from os import sys

web_app = Blueprint(
    'web_app',
    __name__,
    template_folder='templates',
    static_url_path='static'
)

# Default Landing page
@web_app.route('/')
def landing():
    return render_template('landing/index.html')

# Load Login Page
@web_app.route('/cloud')
def cloud():
    return render_template('login.html')

# Load Login Page
@web_app.route('/success')
def trip_board():
    return render_template('success.html')