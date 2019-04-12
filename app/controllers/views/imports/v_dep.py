from flask import render_template, request

from app.controllers.forms.forms import ContatoForm
from app.controllers.functions.email import enviarEmailDM
from app.models.models import *
