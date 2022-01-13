from django.contrib import admin
from .models import Student, Teacher


@admin.register(Teacher)
class TeacherAdminView(admin.ModelAdmin):
    """
        Registering the teacher model in admin panel
    """

    list_display = ('teacher_name', 'subject', 'teachers_students')


@admin.register(Student)
class StudentAdminView(admin.ModelAdmin):
    """
        Registering the student model in admin panel
    """

    list_display = ('student_name', 'roll_num', 'students_teachers')
