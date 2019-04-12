from flask_wtf import FlaskForm, RecaptchaField
from wtforms import BooleanField, SelectField
from wtforms.validators import InputRequired
from app.controllers.functions.form_choices import get_opcoes_camisetas
from app.controllers.constants import *

class ParticipanteForm(FlaskForm):
    kit = BooleanField('Kit', id="kit")
    camiseta = SelectField('Camiseta', choices=get_opcoes_camisetas(
    ), id="camiseta", default="P Feminino", coerce=int)
    restricao_coffee = SelectField(
        'Restrição para o Coffee-Break', choices=escolhas_restricao, default="Nenhum", coerce=int, id="restricao_coffee")
