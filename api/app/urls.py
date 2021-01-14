from django.urls import path
from app import views

# all the api urls
urlpatterns = [
    # returns 1x1 pxl image (invisible unless using microscope)
    path('load_image/<str:i_hash>/', views.load_image, name='load_image'),
    # returns a unique hash
    path('get_image_hash/', views.get_image_hash, name='get_image_hash'),
    # used to check if email has been opened
    path('get_hash_status/<str:i_hash>/', views.get_hash_status, name='get_hash_status'),
]

