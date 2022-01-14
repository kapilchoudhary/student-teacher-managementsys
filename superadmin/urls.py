from unicodedata import name
from django.urls import path
from .views import DashBoard, AllTeachersView, AllStudentsView, DeleteStudentView, DeleteTeacherView

urlpatterns = [
    path('', DashBoard.as_view()),
    path('students/', AllStudentsView.as_view(), name='all_students'),
    path('students/<int:id>', AllStudentsView.as_view(), name='all_students'),
    path('delete_student/<int:id>', DeleteStudentView.as_view(), name='delete_student'),
    path('delete_teacher/<int:id>', DeleteTeacherView.as_view(), name='delete_teacher'),
    path('teachers/', AllTeachersView.as_view(), name='all_teachers'),
    path('teachers/<int:id>', AllTeachersView.as_view(), name='all_teachers'),


]