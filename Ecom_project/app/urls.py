"""
URL configuration for Ecom_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('product_details/<int:pk>',views.ProductDetailsView.as_view(),name='product_details'),
    path('products-title/<val>', views.CategoryTitle.as_view(), name='products-title'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # ? FOR IMAGE URL CONFIG