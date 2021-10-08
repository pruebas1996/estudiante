from django.urls import path

from _estudiantes.views import students_list_create, student_detail

app_name = 'students'

urlpatterns = [
    path('<id>/', student_detail, name='student_detail'),
    path('', students_list_create, name='list_create')
]
