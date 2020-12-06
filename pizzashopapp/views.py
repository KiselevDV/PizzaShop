from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # проверка входа
from .forms import UserForm, PizzaShopForm


def home(request):
    return redirect(pizzashop_home)


@login_required(login_url='/pizzashop/sing-in/')
def pizzashop_home(request):
    return render(request, 'pizzashop/home.html', {})


def pizzashop_sing_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()
    return render(request, 'pizzashop/sing_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    })
