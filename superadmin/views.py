from django.shortcuts import render, redirect, get_object_or_404
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
        if kwargs.get('id'):
            try:
                st_obj = get_object_or_404(Student,id = kwargs.get('id'))
            except Student.DoesNotExist:
                return render(request, template_name='superadmin/students/edit_student.html', context={'msg': 'Student Not Found'})
            
            form = StudentForm(instance=st_obj)
            return render(request, template_name='superadmin/students/edit_student.html', context={'form' : form, 'id' : kwargs.get('id')})

            
        form = StudentForm()
        all_students = Student.objects.values('student_name', 'id', 'roll_num')

        return render(request, template_name=self.template_name, context={'all_students': all_students, 'form': form})

    def post(self, request, *args, **kwargs):

        if kwargs.get('id'):
            st_obj = get_object_or_404(Student,id = kwargs.get('id'))
            form = StudentForm(request.POST,instance=st_obj)
            form.is_valid()
            form.save()
            return redirect('/students/')

        all_students = Student.objects.values('student_name', 'id', 'roll_num')
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()

            return redirect('/students/')

        return render(request, template_name=self.template_name, context={'all_students': all_students, 'form': fm})


class DeleteStudentView(View):

    """
    Delete Student View
    """

    def post(self, request, *args, **kwargs):
        if kwargs.get('id'):
            Student.objects.get(id = kwargs.get('id')).delete()
        return redirect('/students/')


class AllTeachersView(View):

    """
    View, add and assign students to teachers
    """

    template_name = 'superadmin/teachers/view_teachers.html'

    def get(self, request, *args, **kwargs):

        if kwargs.get('id'):
            try:
                tch_obj = get_object_or_404(Teacher,id = kwargs.get('id'))
            except Exception as e:
                return render(request, template_name='superadmin/teachers/edit_teacher.html', context={'msg': 'Teacher Not Found'})
            
            form = TeacherForm(instance=tch_obj)
            return render(request, template_name='superadmin/teachers/edit_teacher.html', context={'form' : form, 'id' : kwargs.get('id')})
        
        form = TeacherForm()
        all_teachers = Teacher.objects.values('teacher_name', 'id', 'subject')

        return render(request, template_name=self.template_name, context={'all_teachers': all_teachers, 'form':  form})

    def post(self, request, *args, **kwargs):

        if kwargs.get('id'):
            tch_obj = get_object_or_404(Teacher,id = kwargs.get('id'))
            form = TeacherForm(request.POST,instance=tch_obj)
            form.is_valid()
            form.save()
            return redirect('/teachers/')

        all_teacher = Teacher.objects.values('teacher_name', 'id', 'subject')

        fm = TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()

            return redirect('/teachers/')

        return render(request, template_name=self.template_name, context={'all_students': all_teacher, 'form': fm})


class DeleteTeacherView(View):

    """
    Delete Teacher View
    """

    def post(self, request, *args, **kwargs):
        if kwargs.get('id'):
            Teacher.objects.get(id = kwargs.get('id')).delete()
        return redirect('/teachers/')