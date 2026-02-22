from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm

def login(request):
    return render(request, "users/login.html")

@login_required
def complete_profile(request):
    if request.method == 'POST':
        major = request.POST.get('major')
        year = request.POST.get('year')

        profile = request.user.profile
        profile.major = major
        profile.year_of_study = year
        profile.save()

        return redirect('home')

    return render(request, 'users/complete_profile.html')

@login_required
def profile(request):
    return render(request, "users/profile.html", {"user": request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form
    }
    return render(request, 'users/edit_profile.html', context)
