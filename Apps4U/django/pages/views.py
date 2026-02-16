from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def starter_pack(request):
    return render(request, 'pages/starter_pack.html')
