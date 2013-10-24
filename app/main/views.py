from flask import Blueprint
from flask import render_template, request, redirect, url_for

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return redirect(url_for('tasks.index'))