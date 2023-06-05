from django.contrib import admin
from .models import Order, OrderItem


# Включение моделей заказа на сайт администрирования
# Класс ModelInline используется с  моделью OrderItem, чтобы включать ее
# внутристрочно в класс OrderAdmin.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    # raw_id_fields - это список полей, которые вы хотите изменить
    # в виджете Input для ForeignKey или ManyToManyField:
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    # Атрибут inlines позволяет вставлять модель
    # в ту же страницу редактирования, что и связанная с ней модель.
    inlines = [OrderItemInline]
