from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

from app.controllers.functions.form_choices import get_opcoes_cotas_patrocinadores, get_opcoes_camisetas
from app.controllers.functions.aux import get_participantes
from app.controllers.constants import *

class PatrocinadorForm(FlaskForm):
    nome_empresa = StringField('Nome', validators=[InputRequired(
        message=ERRO_INPUT_REQUIRED), Length(min=1, max=100)])
    logo = StringField('Logo', validators=[InputRequired(
        message=ERRO_INPUT_REQUIRED), Length(min=1, max=100)])
    ativo_site = BooleanField('Ativo', validators=[InputRequired()], id="ativo_site")
    id_cota = SelectField('Cota', choices=get_opcoes_cotas_patrocinadores(),
        id="cota", default="0", coerce=int)
    link_website = StringField('Site', validators=[InputRequired(
        message=ERRO_INPUT_REQUIRED), Length(min=1, max=200)])


class ComprovanteForm(FlaskForm):
    comprovante = FileField('Comprovante de Pagamento', validators=[
            FileRequired(message=ERRO_INPUT_REQUIRED),
            FileAllowed(['png', 'jpg', 'jpeg'], message=ERRO_EXTENSAO_INVALIDA)
        ])


class AlteraCamisetaForm(FlaskForm):
    participante = SelectField("Selecione o usuário", choices=get_participantes(), id="participante", coerce=int)
    camiseta = SelectField("Modelos", choices=get_opcoes_camisetas(), default="P Feminino", id="camiseta", coerce=int)


class VendaKitForm(FlaskForm):
    participante = SelectField("Inscrições na SECOMP 2019", choices=get_participantes(), id="participante", coerce=int)
    camiseta = SelectField("Modelos", choices=get_opcoes_camisetas(), default="P Feminino", id="camiseta", coerce=int)
