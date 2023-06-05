from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from shop.models import Address
from shop.models import DiscountsIndex


def order_create(request):
    # корзина извлекается из сеанса по средством инструкции cart = Cart(request)
    cart = Cart(request)
    address = Address.objects.all()
    discount = DiscountsIndex.objects.filter(is_published=True)

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
            # очистить корзину
            cart.clear()
            return render(request,
                          'orders/order/created.html',
                          {'order': order, 'address': address, 'discounts': discount})
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form, 'address': address, 'discounts': discount})
