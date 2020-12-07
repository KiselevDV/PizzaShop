from django.http import JsonResponse  # возращает ответ в формате json
from .models import PizzaShop
from .serializers import PizzaShopSerializer


def client_get_pizzashops(request):
    # Метод получает информацию о пиццериях для клиента и возращает ответ в виде json
    pizzashops = PizzaShopSerializer(
        PizzaShop.objects.all().order_by('-id'),
        # many=True - сериализуем запросы вместо экземпляра модели
        many=True,
        # аргумент "context" в дополнение к объекту. В частности для получения гиперссылок
        context={'request': request}
    ).data

    return JsonResponse({'pizzashops': pizzashops})

# Аналог views для REST API
