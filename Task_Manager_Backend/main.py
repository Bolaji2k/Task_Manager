import os
from flask import Flask
from .models import Task, db
from .views import create_view
from .admin import admin
from flask_migrate import Migrate
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "weertyuijkopl"

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, 'data.sqlite')}'
    app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False 
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

    create_view(app)

    db.init_app(app)
    admin.init_app(app)
    migrate = Migrate(app, db)
    CORS(app)

    return app


if __name__ == '__main__':
    app = create_app()
