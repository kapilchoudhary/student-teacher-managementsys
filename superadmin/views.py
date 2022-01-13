from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import StudentForm, TeacherForm
from .models import Student, Teacher


class DashBoard(View):

    """
    Admin/ Teacher DashBoard
    """
    template_name = 'superadmin/dashboard.html'

    def get(self, request, *args, **kwargs):

        return render(request, template_name=self.template_name)


class AllStudentsView(View):

    """
    View and add students 
    """

    template_name = 'superadmin/students/view_students.html'

    def get(self, request, *args, **kwargs):

        form = StudentForm()
        all_students = Student.objects.values('student_name', 'id', 'roll_num')

        return render(request, template_name=self.template_name, context={'all_students': all_students, 'form': form})

    def post(self, request, *args, **kwargs):

        all_students = Student.objects.values('student_name', 'id', 'roll_num')
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()

            return redirect('/students/')

        return render(request, template_name=self.template_name, context={'all_students': all_students, 'form': fm})


class AllTeachersView(View):

    """
    View, add and assign students to teachers
    """

    template_name = 'superadmin/teachers/view_teachers.html'

    def get(self, request, *args, **kwargs):

        form = TeacherForm()
        all_teachers = Teacher.objects.values('teacher_name', 'id', 'subject')

        return render(request, template_name=self.template_name, context={'all_teachers': all_teachers, 'form':  form})

    def post(self, request, *args, **kwargs):

        all_teacher = Teacher.objects.values('teacher_name', 'id', 'subject')

        fm = TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()

            return redirect('/teachers/')

        return render(request, template_name=self.template_name, context={'all_students': all_teacher, 'form': fm})