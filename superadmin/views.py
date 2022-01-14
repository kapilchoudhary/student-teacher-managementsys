from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentForm, TeacherForm, StarStudentForm
from .models import StarStudent, Student, Teacher


class DashBoard(View):

    """
    Admin/ Teacher DashBoard
    """
    template_name = 'superadmin/dashboard.html'

    def get(self, request, *args, **kwargs):

        return render(request, template_name=self.template_name)


class AllStudentsView(LoginRequiredMixin, View):

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


class DeleteStudentView(LoginRequiredMixin, View):

    """
    Delete Student View
    """

    def post(self, request, *args, **kwargs):
        if kwargs.get('id'):
            Student.objects.get(id = kwargs.get('id')).delete()
        return redirect('/students/')


class AllTeachersView(LoginRequiredMixin, View):

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
        all_teachers = Teacher.objects.values('teacher__username', 'id', 'subject')

        return render(request, template_name=self.template_name, context={'all_teachers': all_teachers, 'form':  form})

    def post(self, request, *args, **kwargs):

        if kwargs.get('id'):
            tch_obj = get_object_or_404(Teacher,id = kwargs.get('id'))
            form = TeacherForm(request.POST,instance=tch_obj)
            form.is_valid()
            form.save()
            return redirect('/teachers/')

        all_teacher = Teacher.objects.values('teacher.username', 'id', 'subject')
        fm = TeacherForm(request.POST)
        if fm.is_valid():
            fm.save()

            return redirect('/teachers/')

        return render(request, template_name=self.template_name, context={'all_students': all_teacher, 'form': fm})


class StarStudentView(LoginRequiredMixin, View):

    """
    Teacher will star their student
    """
    template_name = 'superadmin/teachers/star_student.html'

    def get(self, request, *args, **kwargs):

        form = StarStudentForm(request.user)
        star_stud = StarStudent.objects.filter(teacher__teacher = request.user)

        return render(request, template_name=self.template_name,
        context={'form' : form, 'star_stud' : star_stud})
    
    def post(self, request, *args, **kwargs):

        star_obj =  StarStudent.objects.filter(student = request.POST.get('student'))
        if star_obj.exists():
            form = StarStudentForm(request.user, request.POST, instance = star_obj[0])
        else:
            form = StarStudentForm(request.user, request.POST)
        tch_obj = Teacher.objects.get(teacher = request.user)
        if form.is_valid():
            tch = form.save(commit=False)
            tch.teacher = tch_obj
            form.save()
            
        return redirect('/star_student/')



class DeleteTeacherView(LoginRequiredMixin, View):

    """
    Delete Teacher View
    """

    def post(self, request, *args, **kwargs):
        if kwargs.get('id'):
            Teacher.objects.get(id = kwargs.get('id')).delete()
        return redirect('/teachers/')


class TeacherLogin(View):

    """
    Login View For Teacher
    """
    
    form = AuthenticationForm()
    template_name = 'superadmin/teachers/login_teacher.html'

    def get(self, request, *args, **kwargs):

        return render(request, template_name=self.template_name,
        context={'form' :  self.form})
    

    def post(self, request, *args, **kwargs):

        form = AuthenticationForm(request= request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request, self.template_name,
                context={'msg' :  'Username or Password Incorrect'})
        return render(request, self.template_name, context={'form' :  form})


class LogoutView(View):

    """
    This is the logout view for Teacher
    """

    def post(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')