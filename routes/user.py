from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for

from models import User


main = Blueprint('user', __name__)


def current_user():
    uid = session.get('user_id')
    if uid is not None:
        return User.query.get(uid)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/login', methods=['POST'])
def login():
    u = User(request.form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate_login(u):
        session['user_id'] = user.id
        return redirect(url_for('todo.index', username=user.username))
    else:
        return redirect(url_for('user.index'))


@main.route('/user/register')
def register():
    return render_template('register.html')


@main.route('/user/new', methods=['POST'])
def new():
    u = User(request.form)
    if u.validate_register():
        u.save()
        return redirect(url_for('.index'))
    else:
        return redirect(url_for('.register'))
