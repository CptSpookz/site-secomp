from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from flask import render_template, request, redirect, abort, flash
from passlib.hash import pbkdf2_sha256
from werkzeug import secure_filename

from app.controllers.forms import LoginForm
from app.models.models import Usuario, db
