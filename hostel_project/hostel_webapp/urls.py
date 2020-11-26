from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about.html', views.about, name='about'),
    path('login.html', views.login, name='login'),
    path('complaint.html', views.complaint, name='complaint'),
    path('register.html', views.register, name='register'),
    path('g4.html', views.g4, name='g4'),
    path('g5.html', views.g5, name='g5'),
    path('g6.html', views.g6, name='g6'),
    path('b1.html', views.b1, name='b1'),
    path('b2.html', views.b2, name='b2'),
    path('b3.html', views.b3, name='b3'),
    path('b5.html', views.b5, name='b5'),
    path('i2.html', views.i2, name='i2'),
    path('complaintlist.html', views.ComplaintList.as_view, name='complaintlist'),
]
