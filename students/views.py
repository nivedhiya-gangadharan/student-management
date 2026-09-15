from django.shortcuts import get_object_or_404, redirect, render
from .forms import StudentForm
from .models import Student

def student_list(request):
    students = Student.objects.all().order_by("id")
    return render(request, "students/student_list.html", {"students": students})

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "students/add_student.html", {"form": form})

def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
    return redirect("student_list")
