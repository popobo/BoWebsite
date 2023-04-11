from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('generate_menu/', views.generate_menu, name='generate_menu'),
    path('download_menu/<str:filename>/', views.download_menu, name='download_menu'),
    path('menu_generator/', views.menu_generator, name='menu_generator'),
]