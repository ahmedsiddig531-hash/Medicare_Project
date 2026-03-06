from django.contrib import admin
from .models import Department, Doctor, Patient, Appointment
from .models import Article, Comment

admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment)
admin.site.register(Article)
admin.site.register(Comment)
