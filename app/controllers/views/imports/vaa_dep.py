from random import SystemRandom
from flask import render_template, request, redirect, abort, url_for
from flask_login import login_required, current_user

from app.controllers.forms.forms_area_admin import *
from app.models.models import *
