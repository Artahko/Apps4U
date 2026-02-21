from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'pages/home.html')

@login_required
def starter_pack(request):
    return render(request, 'pages/starter_pack.html')
