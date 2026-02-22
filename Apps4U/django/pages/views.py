from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    if request.user.profile.major=="NONE" or request.user.profile.year_of_study==0:
        return redirect('complete_profile')

    return render(request, 'pages/home.html')

@login_required
def starter_pack(request):
    return render(request, 'pages/starter_pack.html')
