from django.db import models
# User - встроенная модель владельца (пользователя)
from django.contrib.auth.models import User


class PizzaShop(models.Model):
    """Модель пиццерии"""
    # related_name - создаёт имя модели для обратной связи от связанной модели,
    # через User можно общаться с PizzaShop (пример: request.user.pizzashop.phone)
    owner = models.OneToOneField(
        User, verbose_name='Владелец', on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField('Название пиццерии', max_length=100)
    phone = models.CharField('Номер телефона', max_length=100)
    address = models.CharField('Адресс пиццерии', max_length=100)
    logo = models.ImageField(
        'Логотип', upload_to='pizzashopapp/pizzashop_logo/', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пиццерия'
        verbose_name_plural = 'Пиццерии'


class Pizza(models.Model):
    pizzashop = models.ForeignKey(PizzaShop, verbose_name='Пиццерия')
    name = models.CharField('Название пиццы', max_length=30)
    description = models.CharField('Описание', max_length=100)
    image = models.ImageField(
        'Изображение пиццы', upload_to='pizzashopapp/pizza_image/', blank=False)
    price = models.PositiveSmallIntegerField('Цена', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'
