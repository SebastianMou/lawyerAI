from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chats/', views.chats, name='chats'),
    path('contracts/', views.contracts, name='contracts'),
    path('contract/<int:pk>/', views.contract, name='contract'),

]