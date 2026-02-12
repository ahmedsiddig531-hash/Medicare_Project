from django.shortcuts import render
rooms = [
    {'id' : 1, 'name' : 'room1'},
     {'id' : 2, 'name' : 'room2'},
      {'id' : 3, 'name' : 'room3'}
]

def home(request):
    return render(request, 'appointments/home.html',{'rooms': rooms})

def doctors(request):
    return render(request, 'appointments/doctors.html')

def book_appointment(request):
    return render(request, 'appointments/book.html')