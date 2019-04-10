#URLs para a área administrativa
from app import app
from app.controllers.views import views_area_administrativa as views

base_url = '/area-administrativa/'

#[{route}, {endpoint}, {view_func}, {methods}]
urls_area_administrativa = [
    ['estoque-camisetas', 'estoque_camisetas', views.estoque_camisetas, ["POST", "GET"]],
    ['estoque-camisetas/<tamanho>', 'estoque_camisetas_por_tamanho', views.estoque_camisetas_por_tamanho, ["POST", "GET"]],
    ['cadastro-patrocinio', 'cadastro_patrocinio', views.cadastro_patrocinio, ["POST", "GET"]],
    ['venda_kits', 'vender_kits', views.vender_kits, ["POST", "GET"]],
    ['fazer-sorteio', 'sortear', views.sortear, ["POST", "GET"]],
    ['fazer-sorteio/do', 'sorteando', views.sorteando, ["POST", "GET"]],
    ['alterar-camiseta', 'alterar_camiseta', views.alterar_camiseta, ["POST", "GET"]]
]

for url in urls_area_administrativa:
    url[0] = base_url + url[0]
