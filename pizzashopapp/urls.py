from django.conf.urls import url
# Для реализации системы входа/выхода (login/logout) - auth_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),

    # АУТЕНТИФИКАЦИЯ
    # Авторизация самого владельца
    url(r'^pizzashop/sign-in/$', auth_views.login,
        {'template_name': 'pizzashop/sign_in.html'},
        name='pizzashop-sign-in'),
    url(r'^pizzashop/sign-out/$', auth_views.logout,
        {'next_page': '/'},
        name='pizzashop-sign-out'),
    url(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),
    # Регистрация нового владельца и его пиццерии
    url(r'^pizzashop/sign-up/$', views.pizzashop_sign_up, name='pizzashop-sign-up'),

    # Меню профиля владельца с возможностью редактирования
    url(r'^pizzashop/account/$', views.pizzashop_account, name='pizzashop-account'),
    # Меню пицц
    url(r'^pizzashop/pizza/$', views.pizzashop_pizza, name='pizzashop-pizza'),

    # Страница для добавления новых пицц
    url(r'^pizzashop/pizza/add/$', views.pizzashop_add_pizza, name='pizzashop-add-pizza'),
]
