from django.shortcuts import render

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