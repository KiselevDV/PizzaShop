from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # проверка входа


def home(request):
    return redirect(pizzashop_home)


@login_required(login_url='/pizzashop/sing-in/')
def pizzashop_home(request):
    return render(request, 'pizzashop/home.html', {})


def pizzashop_sing_up(request):
    return render(request, 'pizzashop/sing_up.html', {})