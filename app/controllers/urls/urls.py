#URLs para informações da SECOMP UFSCar
from app import app
from app.controllers.views import views

urls = [
    ['/', 'index', views.index, ["POST", "GET"]],
    ['/contatoDM', 'contatoDM', views.contatoDM, ["POST", "GET"]],
    ['/constr', 'constr', views.constr, ["POST", "GET"]],
    ['/sobre', 'sobre', views.sobre, ["POST", "GET"]],
    ['/equipe', 'equipe', views.equipe, ["POST", "GET"]],
    ['/faq', 'faq', views.faq, ["POST", "GET"]]
]
