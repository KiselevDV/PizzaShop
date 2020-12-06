from django.db import models
# User - встроенная модель владельца (пользователя)
from django.contrib.auth.models import User


class PizzaShop(models.Model):
    """Модель пиццерии"""
    # related_name - создаёт имя модели для обратной связи от связанной модели
    owner = models.OneToOneField(
        User, verbose_name='Владелец', on_delete=models.CASCADE, related_name='pizzashop')
    name = models.CharField('Название пиццерии', max_length=100)
    phone = models.CharField('Номер телефона', max_length=100)
    address = models.CharField('Адресс пиццерии', max_length=100)
    logo = models.ImageField('Логотип', upload_to='pizzashopapp/pizzashop_logo/', blank=False)

    def __str__(self):
        return self.name
