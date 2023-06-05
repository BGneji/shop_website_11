from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


admin.site.register(TimeSell)
admin.site.register(Address)
admin.site.register(TitleSliderCategory)


@admin.register(BestSellingProducts)
class BestSellingProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'image_show', 'price', 'past_price', 'is_published']
    list_editable = ['is_published']

    # картинка в место ссылки на изображение
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None

    # название столбца c картинкой
    image_show.__name__ = "Картинка"


@admin.register(DiscountsIndex)
class DiscountsIndexAdmin(admin.ModelAdmin):
    list_display = ['title', 'firstorder', 'appdiscounts', 'is_published']


@admin.register(TitleSliderImg)
class TitleSliderImgAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'available', 'image_show']
    readonly_fields = ('image_show',)

    # картинка в место ссылки на изображение
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None

    # название столбца c картинкой
    image_show.__name__ = "Картинка"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    # создания поля slug на базе заголовка(name).
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['image_show', 'name', 'slug', 'price', 'last_price', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    # поля для изменения
    list_editable = ['price', 'slug', 'available', 'last_price']
    # последовательность имен полей, которые должны быть
    # преобразованы в гиперссылки, ведущие на страницу правки записи;
    list_display_links = ('name',)
    # создания поля slug на базе заголовка(name).
    prepopulated_fields = {'slug': ('name', )}

    # картинка в место ссылки на изображение
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None

    # название столбца c картинкой
    image_show.__name__ = "Картинка"


@admin.register(AboutCompanyUser)
class AboutCompanyUserAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image_show']
    list_filter = ('title',)

    # картинка в место ссылки на изображение
    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
        return None
    # название столбца c картинкой
    image_show.__name__ = "Картинка222"

