from django.shortcuts import render
from django.views import generic
from .models import Complaint

class ComplaintList(generic.ListView):
    queryset = Complaint.objects.order_by('date')
    template_name = 'complaintlist.html'
    def as_view(request):
        return render(request, 'complaintlist.html', {})

hostels = [
    'B1',
    'B2',
    'B5'
]


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def login(request):
    return render(request, 'login.html', {})

def complaint(request):
    return render(request, 'complaint.html', {})

def g4(request):
    
    return render(request, 'g4.html', {})

