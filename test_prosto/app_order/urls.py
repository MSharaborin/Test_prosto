from django.urls import path

from . import views


urlpatterns = [
    path('', views.OrderList.as_view(), name='order_list_url'),
    path('order/new/', views.CreateOrder.as_view(), name='create_url'),
    path('order/<int:pk>/edit/', views.UpdateOrder.as_view(), name='update_url'),
    path('order/<int:pk>/', views.DetailOrder.as_view(), name='detail_url'),
    path('order/<int:pk>/delete/', views.DeleteOrder.as_view(), name='delete_url'),
]
