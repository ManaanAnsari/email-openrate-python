from django.urls import path
from app import views


urlpatterns = [
    path('load_image/<str:i_hash>/', views.load_image, name='load_image'),
    path('get_image_hash/', views.get_image_hash, name='get_image_hash'),
    path('get_hash_status/<str:i_hash>/', views.get_hash_status, name='get_hash_status'),
]

