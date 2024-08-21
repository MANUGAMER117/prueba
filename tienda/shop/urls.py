from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_producto, name = 'agregar_producto'),
    path('carrito/agregar/int:producto_id/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/proceso_compra/', views.proceso_compra, name = 'proceso_compra'),
]
