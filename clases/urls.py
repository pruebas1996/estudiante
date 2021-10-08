from django.urls import path

from clases.views import class_list_create

app_name = 'class'

urlpatterns = [
    path('', class_list_create, name='list_class')
]
