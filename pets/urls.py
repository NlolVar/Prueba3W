from django.urls import path
from . import views

urlpatterns =[
    path('index', views.index, name='index'),
    path('reg_prod/', views.reg_prod, name='reg_prod'),
    path('tienda/', views.tienda, name='tienda'),
    path('edit_producto/<int:product_id>/', views.edit_prod, name='edit_producto'),
]