from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_list/', views.order_list, name='order_list'),
    path('create_review/<int:order_id>/', views.create_review, name='create_review'),
]