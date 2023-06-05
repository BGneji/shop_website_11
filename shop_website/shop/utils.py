from .models import Address, DiscountsIndex
from cart.forms import CartAddProductForm


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        discount = DiscountsIndex.objects.filter(is_published=True)
        address = Address.objects.all()
        context['address'] = address
        context['discounts'] = discount
        #cоздание формы для добавление в корзину
        context['cart_product_form'] = CartAddProductForm()
        return context
