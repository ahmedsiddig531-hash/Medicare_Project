from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('doctors/', views.doctors, name='doctors'),

    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),

    path('book/<int:doctor_id>/', views.book_appointment, name='book_appointment'),

    path('success/', views.appointment_success, name='appointment_success'),

    path('appointments/', views.appointment_list, name='appointments'),

    path('wellbeing/', views.wellbeing, name='wellbeing'),

    path('article/<int:article_id>/', views.article_detail, name='article_detail'),

    path('comment/<int:article_id>/', views.add_comment, name='add_comment'),
    path('search/', views.search, name='search'),
    path("register/", views.register, name="register"),

    path("my-appointments/", views.my_appointments, name="my_appointments"),
    path("cancel-appointment/<int:appointment_id>/", views.cancel_appointment, name="cancel_appointment"),
path("live-search/", views.live_search, name="live_search"),
]