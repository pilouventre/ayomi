from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('edit/<int:id>/', views.edit, name='edit'),
]