from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('sing_up', views.RegisterUser.as_view(), name='singup'),
    path('logout', views.logout_user, name='logout'),
    path('category/<slug:cat_slug>/<slug:slug_name>/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:category_slug>/', views.ShowCategory.as_view(), name='category1111'),
    path('about', views.AboutCompany.as_view(), name='about'),
    path('', views.IndexHome.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
