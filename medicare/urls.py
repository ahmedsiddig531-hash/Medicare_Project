from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from appointments import views
urlpatterns = [

 

    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),


    path('', include('appointments.urls')),
    path("my-appointments/", views.my_appointments, name="my_appointments"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)