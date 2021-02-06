from django.urls import path
from .views import index, new_url

urlpatterns = [
    path('', index, name="index"),
    path('<str:id>', new_url, name='new_url'),
]
