from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),
    path('transactions/', views.transactions, name='transactions'),
    path('<int:transaction>/', views.detail, name='detail'),
    path('investment/<int:pk>/delete/', views.delete_transaction, name='delete_transaction'),
]


