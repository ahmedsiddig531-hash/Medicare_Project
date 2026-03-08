from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Doctor, Department, Appointment, Patient, Article, Comment
from .forms import RegisterForm
from django.http import JsonResponse


# ---------------- HOME ----------------

def home(request):

    doctors = Doctor.objects.all()[:4]   
    departments = Department.objects.all()
    articles = Article.objects.all()[:3]

    return render(request, "home.html", {
        "doctors": doctors,
        "departments": departments,
        "articles": articles
    })


# ---------------- SEARCH ----------------

def search(request):
    query = request.GET.get("q")

    doctors = []
    departments = []
    articles = []

    if query:
        doctors = Doctor.objects.filter(
            Q(name__icontains=query) |
            Q(department__name__icontains=query)
        )

        departments = Department.objects.filter(
            name__icontains=query
        )

        articles = Article.objects.filter(
            title__icontains=query
        )

    return render(request, "appointments/search_results.html", {
        "query": query,
        "doctors": doctors,
        "departments": departments,
        "articles": articles
    })

 

def live_search(request):

    query = request.GET.get("q")
    results = []

    if query:
        doctors = Doctor.objects.filter(
            name__icontains=query
        )[:5]

        for doctor in doctors:
            results.append({
                "id": doctor.id,
                "name": doctor.name,
                "department": doctor.department.name
            })

    return JsonResponse(results, safe=False)

# ---------------- REGISTER ----------------

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


# ---------------- DOCTORS ----------------

def doctors(request):

    department_id = request.GET.get("department")

    doctors = Doctor.objects.all()
    departments = Department.objects.all()

    if department_id:
        doctors = doctors.filter(department_id=department_id)

    return render(request, "appointments/doctors.html", {
        "doctors": doctors,
        "departments": departments
    })
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    return render(request, "appointments/doctor_detail.html", {
        "doctor": doctor
    })


# ---------------- BOOK APPOINTMENT ----------------

@login_required
def book_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":

        patient = Patient.objects.create(
            full_name=request.POST["full_name"],
            phone_number=request.POST["phone_number"],
            email=request.POST["email"],
            age=request.POST["age"]
        )

        date = request.POST["appointment_date"]
        time = request.POST["appointment_time"]

        exists = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=date,
            appointment_time=time
        ).exists()

        if exists:
            messages.error(request, "This time slot is already booked")
            return redirect("book_appointment", doctor_id=doctor.id)

        Appointment.objects.create(
            user=request.user,
            patient=patient,
            doctor=doctor,
            appointment_date=date,
            appointment_time=time,
            message=request.POST.get("message", "")
        )

        messages.success(request, "Appointment booked successfully!")
        return redirect("appointment_success")

    return render(request, "appointments/book_appointment.html", {
        "doctor": doctor
    })


# ---------------- MY APPOINTMENTS ----------------

@login_required
def my_appointments(request):
    appointments = Appointment.objects.filter(user=request.user)

    return render(request, "appointments/my_appointments.html", {
        "appointments": appointments
    })


@login_required
def cancel_appointment(request, appointment_id):
    appointment = get_object_or_404(
        Appointment,
        id=appointment_id,
        user=request.user
    )

    appointment.status = "Cancelled"
    appointment.save()

    return redirect("my_appointments")


# ---------------- SUCCESS PAGE ----------------

def appointment_success(request):
    return render(request, "appointments/appointment_success.html")


# ---------------- ALL APPOINTMENTS ----------------

def appointment_list(request):
    appointments = Appointment.objects.all()

    return render(request, "appointments/appointments_list.html", {
        "appointments": appointments
    })


# ---------------- WELLBEING ----------------

def wellbeing(request):
    articles = Article.objects.all()

    return render(request, "appointments/wellbeing.html", {
        "articles": articles
    })


# ---------------- ARTICLES ----------------

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    article.views += 1
    article.save()

    comments = Comment.objects.filter(article=article)

    return render(request, "appointments/article_detail.html", {
        "article": article,
        "comments": comments
    })


def add_comment(request, article_id):
    if request.method == "POST":
        article = get_object_or_404(Article, id=article_id)

        Comment.objects.create(
            article=article,
            name=request.POST["name"],
            text=request.POST["text"]
        )

    return redirect("article_detail", article_id=article_id)