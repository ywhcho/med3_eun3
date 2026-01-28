from django.urls import path
from . import views

app_name = 'medicines'

urlpatterns = [
    path('search/', views.search_view, name='search'),
    path('detail/<int:pk>/', views.detail_view, name='detail'),
]
