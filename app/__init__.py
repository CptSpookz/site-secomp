from flask import Flask, redirect, request
from flask_bootstrap import Bootstrap
from flask_script import Server, Manager, prompt_bool
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from flask_babelex import Babel
import os

configs = {
    'development': '../config/development.py',
    'production': '../config/production.py',
    'default': '../config/default.py'
}

config_name = os.getenv('FLASK_CONFIGURATION', 'development')

app = Flask(__name__)
Bootstrap(app)
babel = Babel(app)
app.config.from_pyfile(configs[config_name])

from app.models.models import db, Usuario

from app.controllers.urls import *
from app.controllers.urls.urls import *
from app.controllers.urls.urls_area_administrativa import *
from app.controllers.urls.urls_participante import *
from app.controllers.urls.urls_login import *

main_route_controller(urls)
main_route_controller(urls_area_administrativa)
main_route_controller(urls_participante)
main_route_controller(urls_login)

migrate = Migrate(app, db)


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def user_loader(user_id):
    return db.session.query(Usuario).filter_by(id = user_id).first()

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect('/login')

from app.controllers import admin

upload_path = os.path.join(os.path.dirname(__file__), 'static')
adm = admin.init_admin(app, upload_path)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0'))

@manager.command
def create():
    "Creates database tables from sqlalchemy models"
    db.create_all()

@manager.command
def drop():
    "Drops database tables"
    if prompt_bool("Erase current database?"):
        db.drop_all()

@babel.localeselector
def get_locale():
    if request.args.get('lang'):
        session['lang'] = request.args.get('lang')
    return "pt"
