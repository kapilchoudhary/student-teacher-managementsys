from django.contrib import admin
from .models import Student, Teacher, StarStudent


@admin.register(Teacher)
class TeacherAdminView(admin.ModelAdmin):
    """
        Registering the teacher model in admin panel
    """

    list_display = ('teacher', 'subject', 'teachers_students')


@admin.register(Student)
class StudentAdminView(admin.ModelAdmin):
    """
        Registering the student model in admin panel
    """

    list_display = ('student_name', 'roll_num', 'students_teachers')


@admin.register(StarStudent)
class StarStudentAdminView(admin.ModelAdmin):
    """
        Registering the star model in admin panel
    """

    list_display = ('student', 'teacher', 'star')
