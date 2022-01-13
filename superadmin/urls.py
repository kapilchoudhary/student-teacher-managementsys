from unicodedata import name
from django.urls import path
from .views import DashBoard, AllTeachersView, AllStudentsView

urlpatterns = [
    path('', DashBoard.as_view()),
    path('students/', AllStudentsView.as_view(), name='all_students'),
    path('teachers/', AllTeachersView.as_view(), name='all_teachers'),

]