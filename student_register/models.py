from django.db import models

class student_register(models.Model):
    
    student_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    email = models.EmailField(unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(blank=True)
    date_of_joining = models.DateField(blank=True)
    qualification = models.CharField(max_length=200, blank=True)
    course = models.CharField(max_length=200, blank=True)
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=80, blank=True)
    resume = models.FileField(upload_to='resumes/', default='')
    reference_id = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = 'resume'
