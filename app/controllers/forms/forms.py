from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField
from wtforms.validators import InputRequired, Length
from app.controllers.constants import *

class ContatoForm(FlaskForm):
    nome_completo = StringField('Nome', validators=[InputRequired(
        message=ERRO_INPUT_REQUIRED), Length(min=1, max=30)])
    email = StringField('Email', validators=[InputRequired(
        message=ERRO_INPUT_REQUIRED), Length(min=1, max=30)])
    mensagem = StringField('Mensagem', validators=[InputRequired(
        message=ERRO_INPUT_REQUIRED), Length(min=1, max=500)])
