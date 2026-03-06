from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Appointment, Doctor, Patient


def home(request):
    return render(request, 'appointments/home.html')

from .models import Doctor, Department


def doctors(request):

    departments = Department.objects.all()

    doctors = None

    department_id = request.GET.get('department')

    if department_id:
        doctors = Doctor.objects.filter(department_id=department_id)

    return render(
        request,
        'appointments/doctors.html',
        {
            'departments': departments,
            'doctors': doctors
        }
    )

def book_appointment(request):

    doctors = Doctor.objects.all()

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        age = request.POST.get("age")

        appointment_date = request.POST.get("appointment_date")
        appointment_time = request.POST.get("appointment_time")

        doctor_id = request.POST.get("doctor")

        doctor = Doctor.objects.get(id=doctor_id)

        patient = Patient.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            email=email,
            age=age
        )

        Appointment.objects.create(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        )

        messages.success(request, "Appointment booked successfully!")

        return redirect('success')

    return render(request, 'appointments/book.html', {'doctors': doctors})


def success_page(request):
    return render(request, 'appointments/success.html')
def wellbeing(request):
    return render(request, 'appointments/wellbeing.html')  

from .models import Article, Comment


def wellbeing(request):

    articles = Article.objects.all()

    return render(request, 'appointments/wellbeing.html', {'articles': articles})

def article_detail(request, id):

    article = Article.objects.get(id=id)

    # زيادة عدد المشاهدات
    article.views += 1
    article.save()

    comments = Comment.objects.filter(article=article)

    return render(
        request,
        'appointments/article_detail.html',
        {
            'article': article,
            'comments': comments
        }
    )

def add_comment(request, id):

    article = Article.objects.get(id=id)

    if request.method == "POST":

        name = request.POST.get("name")
        text = request.POST.get("text")

        Comment.objects.create(
            article=article,
            name=name,
            text=text
        )

    return redirect('article_detail', id=id)

