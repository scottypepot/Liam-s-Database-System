from django.shortcuts import render
from .models import Branch

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'branch/branch_list.html', {'branches': branches})
