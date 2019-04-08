from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from bcrypt import gensalt
from flask import render_template, request, redirect, abort, flash
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from passlib.hash import pbkdf2_sha256
from werkzeug import secure_filename

from app.controllers.forms import LoginForm
from app.models.models import Usuario, db

def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = db.session.query(Usuario).filter_by(
            email=form.email.data).first()
        if user:
            if pbkdf2_sha256.verify(form.senha.data, user.senha):
                user.autenticado = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect(url_for('dashboard_usuario'))
    return render_template('login.html', form=form)


@login_required
def logout():
    """
    Renderiza a página de logout do projeto
    """
    user = current_user
    user.autenticado = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))
