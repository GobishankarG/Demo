from django.urls import path
from .import views

urlpatterns = [
    path('', views.create_student_register, name='create-student_register'),
    path('search/', views.search_student_register, name='search-student_register'),
    path('update/<int:pk>', views.update_student_register, name='update-student_register'),
    path('delete/<int:pk>', views.delete_student_register, name='delete-student_register'),
]
