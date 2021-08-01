from django.urls import path
from .views import index, register_account

app_name = 'todolist'

urlpatterns = [
    path('', index, name='todolist'),
    path('register/', register_account, name='register')
]
