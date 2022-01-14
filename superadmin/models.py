from django.db import models


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

        return ", ".join([str(tch['teacher_name']) for tch in self.student_teacher.values('teacher_name')])
    
    def save(self, *args, **kwargs):
        if not self.roll_num:
            self.roll_num = Student.objects.count() + 1
        return super().save(*args, **kwargs)


class Teacher(models.Model):

    """
    Teacher Model having foreignkey relationship with User model
    and many to many relationship with students
    """

    teacher_name = models.CharField(max_length=20, blank=False, null=False)
    subject = models.CharField(max_length=20, blank=False, null=False)

    students = models.ManyToManyField(Student, related_name='student_teacher')

    def __str__(self) -> str:
        return f'{self.teacher_name}'

    def teachers_students(self):
        """ Method for getting all the students of each teacher """

        return ", ".join([str(std['student_name']) for std in self.students.values('student_name')])
