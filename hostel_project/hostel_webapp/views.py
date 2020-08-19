from django.shortcuts import render


hostels = [
    'B1',
    'B2',
    'B5'
]


# Create your views here.
def home(request):
    return render(request, 'hostel_webapp/home.html', {'hostels': hostels})
