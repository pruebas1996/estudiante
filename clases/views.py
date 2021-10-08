from django.shortcuts import render

# Create your views here.
from clases.models import Clase


def class_list_create(request):
    if request.method == 'POST':
        new_class = {
            'name': request.POST['name'],
            'theme': request.POST['theme'],
            'schedule': request.POST['schedule']
        }
        Clase.objects.create(**new_class)
    lessons = Clase.objects.all()
    context = {
        'lessons': lessons
    }
    return render(request, 'clases/list_clases.html', context)
