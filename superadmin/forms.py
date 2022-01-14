from dataclasses import field
from django import forms
from .models import StarStudent, Student, Teacher
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentForm(forms.ModelForm):

    """ 
    Student Form
    """
    
    student_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))


    class Meta:
        model = Student
        fields = ('student_name',)


class TeacherForm(forms.ModelForm):

    """ 
    Teacher Form
    """

    teacher = forms.ModelChoiceField(queryset=User.objects.all(),
                                    to_field_name = 'username',
                                    empty_label="Select Teacher")

    # teacher_name = forms.CharField(widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'required': 'true'}))

    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))

    students = forms.ModelMultipleChoiceField(queryset= Student.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Teacher
        fields = ('teacher', 'subject', 'students')


class StarStudentForm(forms.ModelForm):

    class Meta:
        model = StarStudent
        fields = ('student', 'star')

    def __init__(self, user, *args, **kwargs):
        super(StarStudentForm, self).__init__(*args, **kwargs)
        tch_obj = Teacher.objects.filter(teacher = user)[0]
        self.fields['student'].queryset = tch_obj.students.all()
    