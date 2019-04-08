from app import app

def main_route_controller(urls):
    for url in urls:
        #app.add_url_rule(url{string}, endpoint{string}, view_func={function}, methods={list})
        app.add_url_rule(url[0], url[1], view_func=url[2], methods=url[3])
