from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=200)
    experience = models.IntegerField()
    hospital = models.CharField(max_length=200)
    available_days = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.full_name


  

class Appointment(models.Model):

    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    message = models.TextField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} with {self.doctor}"

class Article(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()

    image = models.ImageField(upload_to='articles/', blank=True, null=True)

    category = models.CharField(max_length=100)

    views = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name