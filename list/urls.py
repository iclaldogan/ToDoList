from django.urls import path
from . import views

urlpatterns = [
    path('', views.gorev_list, name='gorev_list'),
    path('ekle/', views.gorev_ekle, name='gorev_ekle'),
    path('guncelle/<int:pk>/', views.gorev_guncelle, name='gorev_guncelle'),
    path('sil/<int:pk>/', views.gorev_sil, name='gorev_sil'),
]
