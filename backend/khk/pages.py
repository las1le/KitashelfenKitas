from flask import Blueprint, render_template

bp = Blueprint('pages', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/ask-for-help')
def ask_for_help():
    return render_template('ask-for-help.html')
