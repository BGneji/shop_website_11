from .cart import Cart

# с помощью него можно получать доступ к корзине в любом шаблоне.
# Внутри каталога приложения cart создайте новый файл и  назовите его
def cart(request):
    return {'cart': Cart(request)}