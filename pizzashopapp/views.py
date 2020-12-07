from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required  # проверка входа
from django.contrib.auth.models import User
from .forms import UserForm, UserFormForEdit, PizzaShopForm, PizzaForm


def home(request):
    return redirect(pizzashop_home)


@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_home(request):
    return redirect(pizzashop_pizza)


@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_account(request):
    # Меню профиля владельца
    # instance - получение данных из БД и подставление их в форму UserFormForEdit
    user_form = UserFormForEdit(instance=request.user)
    pizzashop_form = PizzaShopForm(instance=request.user.pizzashop)

    # Редактирование части данных о владельце
    # Если были внесены правки в форме и отравлены на обновление (POST)
    if request.method == "POST":
        # Собирает новые данные из полей при редактировании, остальные (неизменённые данные) из БД
        user_form = UserFormForEdit(request.POST, instance=request.user)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES, instance=request.user.pizzashop)

        if user_form.is_valid() and pizzashop_form.is_valid():
            # Если формы валидны сохраняет в БД
            user_form.save()
            pizzashop_form.save()

    return render(request, 'pizzashop/account.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    })


@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_pizza(request):
    # Меню пицц
    return render(request, 'pizzashop/pizza.html', {})


@login_required(login_url='/pizzashop/sign-in/')
def pizzashop_add_pizza(request):
    # Добавление новых пицц
    # PizzaForm() - вызов пустой формы
    pizza_form = PizzaForm()

    if request.method == 'POST':
        # PizzaForm(request.POST, request.FILES) вызов формы и заполнение её днными
        # request.POST - текст, request.FILES - медиа
        pizza_form = PizzaForm(request.POST, request.FILES)

        if pizza_form.is_valid():
            pizza = pizza_form.save(commit=False)  # Приостановка сохранения
            # Привязываем пиццерию с пиццей
            # Добавляем данные о пиццерии в поле пиццерии в модели пиццы
            pizza.pizzashop = request.user.pizzashop
            pizza.save()
            return redirect(pizzashop_pizza)

    return render(request, 'pizzashop/add_pizza.html', {'pizza_form': pizza_form})


def pizzashop_sign_up(request):
    # Регистрация нового владельца и его пиццерии
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        # request.FILES - для получения логотипа (model PizzaShop поле logo)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)
            new_pizzashop.owner = new_user
            new_pizzashop.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password'],
            ))

            return redirect(pizzashop_home)

    return render(request, 'pizzashop/sign_up.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form,
    })
