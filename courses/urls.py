# course_registration/urls.py

from django.urls import path
from .views import  add_course, delete_course, add_student, drop_student, course_list

urlpatterns = [
    path('list/', course_list, name='course_list'),
    path('add/', add_course, name='add_course'),
    path('delete/<str:course_id>/', delete_course, name='delete_course'),
    path('add_student/<str:course_id>/', add_student, name='add_student'),
    path('drop_student/<str:course_id>/', drop_student, name='drop_student'),
]
