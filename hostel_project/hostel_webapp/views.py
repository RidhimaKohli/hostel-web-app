from django.shortcuts import render


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
