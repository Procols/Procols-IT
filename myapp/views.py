from django.shortcuts import render
from .models import ContactInfo

def index(request):
    return render(request, 'index.html')

def service(request):
    return render(request, 'service.html')

def seo(request):
    return render(request, 'seo.html')

def webapp(request):
    return render(request, 'webapp.html')

def digitalmarketing(request):
    return render(request, 'digitalmarketing.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')


def contactinfo_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        details = request.POST.get('details')
        ContactInfo.objects.create(email=email, details=details)
        return render(request, 'index.html', {'message': 'Submitted successfully!'})
    return render(request, 'contactus.html')