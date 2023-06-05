from django.db import models
from django.urls import reverse


class BestSellingProducts(models.Model):
    title = models.CharField('Название', max_length=150)
    price = models.CharField('Цена', max_length=150)
    past_price = models.CharField('Прошлая цена', max_length=150)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image/best_selling/')

    class Meta:
        verbose_name = 'Лучшее предложение'
        verbose_name_plural = 'лучшие предложения'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='image/category/', null=True)

    class Meta:
        # ***сортировка по имени ***
        ordering = ('name',)
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category1111', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey('Category',
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    last_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='image/product/', null=True)
    image1 = models.ImageField(upload_to='image/product/', null=True)
    image2 = models.ImageField(upload_to='image/product/', null=True)
    image3 = models.ImageField(upload_to='image/product/', null=True)
    image4 = models.ImageField(upload_to='image/product/', null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        print(self.category.name)
        return f'{self.name} | {self.category.name}'

    def get_absolute_url(self):
        # return reverse('product_detail1', args=[str(self.id)])
        return reverse('product_detail', kwargs={"cat_slug": self.category.slug, 'slug_name': self.slug, 'pk': self.id})


class Address(models.Model):
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    index = models.DecimalField(decimal_places=0, max_digits=6)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20, default=True)
    link = models.CharField(max_length=20, default=True)

    def __str__(self):
        return self.country


class TitleSliderCategory(models.Model):
    title = models.CharField('Название слайдера', max_length=150)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Слайдер вначале'
        verbose_name_plural = 'Слайдеры вначале'

    def __str__(self):
        return self.title


class TitleSliderImg(models.Model):
    category = models.ForeignKey(TitleSliderCategory,
                                 related_name='TitleSliderCategory',
                                 on_delete=models.CASCADE)
    title = models.CharField('Название картинки для слайдера', max_length=255)
    description = models.TextField(max_length=1000, blank=True)
    available = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='image/titleslider/', null=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'Настройка слайдера'
        verbose_name_plural = 'Настройка слайдера'

    def __str__(self):
        return self.title


class DiscountsIndex(models.Model):
    title = models.CharField(max_length=100, default=True)
    firstorder = models.CharField(max_length=10)
    appdiscounts = models.CharField(max_length=10)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.firstorder


class TimeSell(models.Model):
    title = models.CharField('Название скидки', max_length=120)
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.title}, {self.date}'


class AboutCompanyUser(models.Model):
    title = models.CharField('Название истории', max_length=100)
    description = models.TextField('Сама история', max_length=1000)
    image = models.ImageField(upload_to='image/about/imageall/', null=True)

    def __str__(self):
        return f'{self.title}'

