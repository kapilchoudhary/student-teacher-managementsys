from django import forms
from .models import Student, Teacher


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

    teacher_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))

    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'required': 'true'}))

    students = forms.ModelMultipleChoiceField(queryset= Student.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Teacher
        fields = ('teacher_name', 'subject', 'students')
