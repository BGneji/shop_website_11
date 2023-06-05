from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View
from cart.forms import CartAddProductForm


from .forms import RegisterUserForm, LoginUserForm
from .models import BestSellingProducts, Category, Product, TitleSliderImg, AboutCompanyUser

from django.views.generic import DetailView, ListView, CreateView

from .utils import DataMixin


class IndexHome(DataMixin, ListView):
    """ Создание представления главной страницы"""
    model = Product
    template_name = 'shop/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bestselling'] = BestSellingProducts.objects.order_by('?')[:5]
        context['categoris'] = Category.objects.order_by('id')
        context['sliders'] = TitleSliderImg.objects.all()
        context['products1'] = Product.objects.order_by('?')[:10]
        # # передача формы количества товара в карзину
        # context['cart_product_form'] = CartAddProductForm()

        c_def = self.get_user_context(title='Главная страница1')
        return dict(list(context.items())+list(c_def.items()))


class ShowCategory(DataMixin, ListView):
    """Создание пердаствления товара по конкретной категории"""
    model = Category
    template_name = 'shop/detail_category_view.html'
    context_object_name = 'categories_product_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cart_product_form'] = CartAddProductForm()
        t_def = self.get_user_context(title='Главная страница3')
        return dict(list(context.items())+list(t_def.items()))

    def get_queryset(self):
                                   # это название модели
        # return Product.objects.filter(category__slug=self.kwargs['category_slug'])
        #                               это название модели                 ORM оптимизирует запросы к связанным моделям
        return Product.objects.filter(category__slug=self.kwargs['category_slug']).select_related('category')


def CartUser(request):
    return render(request, 'shop/cart.html',)


class AboutCompany(DataMixin, ListView):
    """Создание представления о Компании"""
    model = AboutCompanyUser
    template_name = 'shop/about.html'
    context_object_name = 'about_company_user_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        t_def = self.get_user_context(title='О компании')
        return dict(list(context.items())+list(t_def.items()))



class RegisterUser(DataMixin, CreateView):
    """Создание представлния для регистрации новго пользователя"""
    form_class = RegisterUserForm
    template_name = 'shop/sing_up.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Страница регистрации')
        return dict(list(context.items())+list(c_def.items()))

    # при успешной регистрации пользователя он залогиниться
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    """Создание представления для авторизации пользователя"""
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Страница авторизации')
        return dict(list(context.items())+list(c_def.items()))

    # перенаправление на главную страницу после авторизации
    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    """Функция для выхода из логина"""
    logout(request)
    return redirect('login')


class ProductDetailView(DataMixin, DetailView):
    """Создание представления для детальной информации о товаре"""
    model = Product
    template_name = 'shop/product_detail.html'
    context_object_name = 'products_detail_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category__slug=self.kwargs['cat_slug']).select_related('category')
        # context['cart_product_form'] = CartAddProductForm()

        # ко всем продуктам мы добавляем категории
        # context['products'] = Product.objects.all().select_related('category')
        # context['cat'] = Category.objects.all()

        c_def = self.get_user_context(title='Страница продукта')
        return dict(list(context.items()) + list(c_def.items()))

    # def get(self, request, slug_name, pk):
    #     product = Product.objects.get(slug=slug_name, id=pk)
    #     context_address = Address.objects.all()
    #     discount = DiscountsIndex.objects.filter(is_published=True)
    #     c_def = self.get_user_context(title=f'Страница О товаре {slug_name}')
    #
    #     return render(request, 'shop/product_detail.html', {"product_list": product, 'c_def_list': c_def,
    #                                                         'context_address_list': context_address,
    #                                                         'discount_list': discount})


































# def index(request):
#     bestselling = BestSellingProducts.objects.all()
#     product = Product.objects.all()
#     categori = Category.objects.order_by('name')
#     data = {
#         'title': 'Главная страница!',
#         'bestselling': bestselling,
#         'categoris': categori,
#         'products': product,
#     }
#     return render(request, 'shop/index.html', data)


# def show_category(request, category_id):
#     bestselling = BestSellingProducts.objects.all()
#     product = Product.objects.filter(category=category_id)
#     categori = Category.objects.all()
#
#     data = {
#         'title': 'Главная страница!',
#         'bestselling': bestselling,
#         'categoris': categori,
#         'products': product,
#     }
#     return render(request, 'shop/detail_category_view.html', context=data)