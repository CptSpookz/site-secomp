from app import app
def main_route_controller(urls):
    for url in urls:
        #app.add_url_rule(url{string}, endpoint{string}, view_func={function}, methods={list})
        app.add_url_rule(url[0], url[1], view_func=url[2], methods=url[3])

from app.controllers.urls.urls import urls
from app.controllers.urls.urls_area_administrativa import urls_area_administrativa as urls_aa
from app.controllers.urls.urls_participante import urls_participante as urls_p
from app.controllers.urls.urls_login import urls_login as urls_l
