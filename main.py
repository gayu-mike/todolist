from flask import Flask
from flask import render_template

from routes.todo import main as todo_routes
from routes.user import main as user_routes


app = Flask(__name__)

app.secret_key = 'secret*key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(user_routes)


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
    app.run(**config)
