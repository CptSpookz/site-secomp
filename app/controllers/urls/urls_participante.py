#URLs do participante
from app import app
from app.controllers.views import views_participante as views

base_url = '/participante/'

#[{route}, {endpoint}, {view_func}, {methods}]
urls_participante = [
    ['cadastro', 'cadastro', views.cadastro, ["POST", "GET"]],
    ['verificar-email', 'verificar_email', views.verificar_email, ["POST", "GET"]],
    ['cadastro-participante', 'cadastro_participante', views.cadastro_participante, ["POST", "GET"]],
    ['dashboard', 'dashboard_usuario', views.dashboard_usuario, ["POST", "GET"]],
    ['enviar-comprovante', 'envio_comprovante', views.envio_comprovante, ["POST", "GET"]],
    ['verificacao/<token>', 'verificacao', views.verificacao, ["POST", "GET"]],
    ['inscricao-atividades', 'inscricao_atividades', views.inscricao_atividades, ["POST", "GET"]],
    ['inscricao-atividades/<filtro>', 'inscricao_atividades_com_filtro', views.inscricao_atividades_com_filtro, ["POST", "GET"]],
    ['inscrever-atividade/<id>', 'inscrever', views.inscrever, ["POST", "GET"]],
    ['desinscrever-atividade/<id>', 'desinscrever', views.desinscrever, ["POST", "GET"]],
    ['alterar-senha', 'alterar_senha', views.alterar_senha, ["POST", "GET"]],
    ['esqueci-senha', 'esqueci_senha', views.esqueci_senha, ["POST", "GET"]],
    ['confirmar-alteracao-senha/<token>', 'confirmar_alteracao_senha', views.confirmar_alteracao_senha, ["POST", "GET"]]
]

for url in urls_participante:
    url[0] = base_url + url[0]
