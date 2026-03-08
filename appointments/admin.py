from django.contrib import admin
from .models import Department, Doctor, Patient, Appointment, Article, Comment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('doctor', 'status', 'appointment_date')
    search_fields = ('patient__full_name', 'doctor__name')


admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Article)
admin.site.register(Comment)