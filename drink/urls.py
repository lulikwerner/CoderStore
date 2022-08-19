from django.urls import path
from drink.views import drinks, delete_drinks, edit_drinks, form_drinks, list_drinks




urlpatterns = [
    path('drinks/', list_drinks, name='drinks'),
    path('create-drinks/', form_drinks, name = 'create-drinks'),
    path('edit-drinks/<int:pk>/', edit_drinks, name='edit-drinks'),
    path('delete-drinks/<int:pk>/', delete_drinks, name='delete-drinks'),
]