from rest_framework import serializers
from .models import PizzaShop


class PizzaShopSerializer(serializers.ModelSerializer):
    """Пиццерии"""
    # SerializerMethodField - используется только для чтения, для добавления данных в
    # сериализованное представление объекта
    logo = serializers.SerializerMethodField()

    def get_logo(self, pizzashop):
        # Получаем "request" и записываем в переменную "request"
        request = self.context.get('request')
        # Саму ссылку на логотип, локальный url (без http://127.0.0.1:8000/)
        logo_url = pizzashop.logo.url
        # request.build_absolute_uri - получение абсолютного url (полный адрес)
        return request.build_absolute_uri(logo_url)

    class Meta:
        model = PizzaShop
        fields = ('id', 'name', 'phone', 'address', 'logo')

# Пример селлиаризатора без наличия модели - наследование от встроенного "Serializer"
# class PizzaShopSerializer(serializers.Serializer):
#     # Указываем поля для преобразрвания в json (аналогично моделям)
#     # allow_blank - может ли быть поле пустым, read_only - только для чтения
#     # allow_empty_file - может ли отсутсвовать файл
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=False, max_length=100, allow_blank=True)
#     phone = serializers.CharField(max_length=100)
#     address = serializers.CharField(max_length=100)
#     logo = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

# Аналог forms для REST API
