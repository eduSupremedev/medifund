from django.shortcuts import render

def base(request):
    return render(request, 'dashboard.html') 

def dashboard(request):
    return render(request, 'dashboard.html')