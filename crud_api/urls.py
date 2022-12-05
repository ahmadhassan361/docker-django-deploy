from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='urls'),
    path('create/', views.add_product, name='add-product'),
    path('product/', views.view_product, name='view-product'),
    path('product/<int:pk>', views.view_single_product, name='view-single-product'),
    path('update/<int:pk>/', views.update_product, name='update-product'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete-product'),

]