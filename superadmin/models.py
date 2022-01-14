from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Student(models.Model):

    """
    Student Model having foreignkey relationship with
    User model and many to many relationship with teacher
    """
    
    student_name = models.CharField(max_length=20, blank=False, null=False)
    roll_num = models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return f'{self.student_name}'

    def students_teachers(self):
        """ Method for getting all the teachers of each student """

        return ", ".join([str(tch['teacher__username']) for tch in self.student_teacher.values('teacher__username')])
    
    def save(self, *args, **kwargs):
        if not self.roll_num:
            self.roll_num = Student.objects.count() + 1
        return super().save(*args, **kwargs)


class Teacher(models.Model):

    """
    Teacher Model having foreignkey relationship with User model
    and many to many relationship with students
    """

    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_admin')

    subject = models.CharField(max_length=20, blank=False, null=False)

    students = models.ManyToManyField(Student, related_name='student_teacher')

    def __str__(self) -> str:
        return f'{self.teacher.username}'

    def teachers_students(self):
        """ Method for getting all the students of each teacher """

        return ", ".join([str(std['student_name']) for std in self.students.values('student_name')])


class StarStudent(models.Model):

    """
    Star a student by Teacher
    """

    STAR = (
        ('NO_STAR', 'NO_STAR'),
        ('STAR', 'STAR'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_star')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_star')
    star = models.CharField(max_length=10, choices=STAR, default='NO_STAR')

    def __str__(self) -> str:
        return self.student.student_name
    
    class Meta:
        verbose_name = 'Star Student'