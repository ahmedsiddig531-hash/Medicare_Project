from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('doctors/', views.doctors, name='doctors'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('success/', views.success_page, name='success'),
    path('wellbeing/', views.wellbeing, name='wellbeing'),
    path('wellbeing/', views.wellbeing, name='wellbeing'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),
    path('comment/<int:id>/', views.add_comment, name='add_comment'),
]



