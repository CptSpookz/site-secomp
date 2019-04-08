from flask import render_template, request, redirect, abort, url_for, Blueprint
from flask_login import login_required, login_user, logout_user, current_user

from app.controllers.forms import *
from app.controllers.functions import *
from app.models.models import *
from os import path, makedirs

def index():
    """
    Renderiza a página inicial do projeto
    """
    return render_template('index.html', title='Página inicial',
                           secomp_now=secomp_now[0], secomp=secomp[0],
                           secomp_email=secomp_email,
                           secompEdition=secomp_edition)

def contatoDM():
    """
    Página de contato
    """
    form = ContatoForm(request.form)
    if form.validate_on_submit():
        nome = form.nome_completo.data
        email = form.email.data
        mensagem = form.mensagem.data
        enviarEmailDM(app, nome, email, mensagem)
        return render_template('contato.html', form=form, enviado=True)
    return render_template('contato.html', form=form)

def constr():
    return render_template('em_constr.html', title='Página em construção')

def sobre():
    return render_template('sobre.html', title='Sobre a Secomp')

def equipe():
    import json
    with open('./config/membros_org.json', 'r') as read_file:
        data = json.load(read_file)
    return render_template('equipe.html', title='Equipe', data=data)

def faq():
    return render_template('faq.html', title='FAQ')
