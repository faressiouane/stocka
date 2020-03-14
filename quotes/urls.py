from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name = "home"),
    path('stock', views.stock, name = "stock"),

]