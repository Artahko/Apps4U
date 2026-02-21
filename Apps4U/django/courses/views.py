from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Activity, Material
from django.views.generic.edit import CreateView
from .forms import CommentForm, MaterialForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

@login_required
def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def course_faq(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/faq.html', {'course': course})

@login_required
def course_activities(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'activities/activities.html', {'course': course})

@login_required
def activity_detail(request, course_slug, activity_id):
    course = get_object_or_404(Course, slug=course_slug)
    activity = get_object_or_404(Activity, id=activity_id)

    return render(request, 'activities/detail_activity.html', {
        'course': course,
        'activity': activity,
    })

def add_material(request, course_slug, activity_id):
    activity = get_object_or_404(Activity, id=activity_id, course__slug=course_slug)

    if request.method == "POST":
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.activity = activity # Link it to the activity
            material.save()
            # Send them back to the detail page after saving
            return redirect('activity_detail', course_slug=course_slug, activity_id=activity_id)
    else:
        form = MaterialForm()

    return render(request, 'activities/add_material.html', {'form': form, 'activity': activity})


def add_comment(request, course_slug, activity_id):
    course = get_object_or_404(Course, slug=course_slug)
    activity = get_object_or_404(Activity, id=activity_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.post = activity

            if request.user.is_authenticated:
                comment.name = request.user.username
            else:
                comment.name = "Anonymous"

            comment.save()
            return redirect('activity_detail', course_slug=course.slug, activity_id=activity.id)
    else:
        form = CommentForm()

    return render(request, 'activities/add_comment.html', {
        'form': form,
        'activity': activity,
        'course': course
    })
