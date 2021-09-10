from flask import Flask, request, redirect
from flask.helpers import url_for
from database.db import db
from blueprints.movie import MOVIES_BOOKPRINT


app = Flask(__name__)
app.config.from_pyfile('config/settings.staging.cfg')
db.init_app(app)

app.register_blueprint(MOVIES_BOOKPRINT, url_prefix='/movies')

@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def home():
    return redirect(url_for('movies.movies_list'))


if __name__ == '__main__':
    app.run()
