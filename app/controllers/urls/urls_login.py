#URLs para lidar com login
from app import app
from app.controllers.views import views_login as views

#[{route}, {endpoint}, {view_func}, {methods}]
urls_login = [
    ['/login', 'login', views.login, ["POST", "GET"]],
    ['/logout', 'logout', views.logout, ["POST", "GET"]]
]
