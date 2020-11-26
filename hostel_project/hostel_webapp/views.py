from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from django.utils import timezone
from .models import Complaint,Student
from .forms import ComplaintForm,StudentForm
from django.views.decorators.csrf import csrf_exempt



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
    if request.method == "POST":
        form = ComplaintForm(request.POST,request.FILES)
        if form.is_valid():
            complaint.student = request.student
            complaint = form.save(commit=False)
            complaint.save()
            return redirect('complaint.html')

    else:
        form = ComplaintForm()
    return render(request, 'complaint.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('register')

    else:
        form = StudentForm()
    return render(request, 'home.html', {'form': form})

def g4(request):
    return render(request, 'g4.html', {})

def b1(request):
    
    return render(request, 'b1.html', {})

def b2(request):
    
    return render(request, 'b2.html', {})

def b3(request):
    
    return render(request, 'b3.html', {})

def b5(request):
    
    return render(request, 'b5.html', {})

def g5(request):
    
    return render(request, 'g5.html', {})

def g6(request):
    
    return render(request, 'g6.html', {})

def i2(request):
    
    return render(request, 'i2.html', {})

