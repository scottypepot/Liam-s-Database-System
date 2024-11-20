from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard.html')  # Reference the correct location of dashboard.html
