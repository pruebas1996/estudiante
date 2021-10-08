from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from _estudiantes.models import Etudiantes


def student_detail(request, id):
    student = get_object_or_404(Etudiantes, id=id)
    if request.method == 'GET':
        context = {
            'student': student
        }
        return render(request, '_estudiantes/detail.html', context)
    if request.method == 'POST':
        student.delete()
        return redirect('students:list_create')


def students_list_create(request):
    if request.method == 'POST':
        new_students = {
            'identification': request.POST['identification'],
            'name': request.POST['name'],
            'lastName': request.POST['lastName'],
            'email': request.POST['email'],
            'telephone': request.POST['telephone'],
            'address': request.POST['address'],
            'DateOfBirth': request.POST['dateOfBirth'],
        }
        Etudiantes.objects.create(**new_students)

    students = Etudiantes.objects.all()
    context = {
        'students': students
    }
    return render(request, '_estudiantes/list_create_students.html', context)
