from django.conf.urls import url
# Для реализации системы входа/выхода (login/logout) - auth_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # АУТЕНТИФИКАЦИЯ
    # Авторизация самого владельца и его пиццерии
    url(r'^pizzashop/sing-in/$', auth_views.login,
        {'template_name': 'pizzashop/sing_in.html'},
        name='pizzashop-sing-in'),
    url(r'^pizzashop/sing-out/$', auth_views.logout,
        {'next_page': '/'},
        name='pizzashop-sing-out'),
    url(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),
    # Регистрация самого владельца и его пиццерии
    url(r'^pizzashop/sing-up/$', views.pizzashop_sing_up, name='pizzashop-sing-up'),
]
