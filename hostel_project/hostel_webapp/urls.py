from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('login.html', views.login, name='login'),
    path('complaint.html', views.complaint, name='complaint'),
    path('register.html', views.register, name='register'),
    path('g4.html', views.g4, name='g4'),
    path('complaintlist.html', views.ComplaintList.as_view, name='complaintlist'),
]
