from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Activity, Comment
from django.views.generic.edit import CreateView
from .forms import CommentForm
from django.urls import reverse


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})


def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/course_detail.html', {'course': course})


def course_faq(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/faq.html', {'course': course})


def course_activities(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'activities/activities.html', {'course': course})


def activity_detail(request, course_slug, activity_id):
    course = get_object_or_404(Course, slug=course_slug)
    activity = get_object_or_404(Activity, id=activity_id)

    return render(request, 'activities/detail_activity.html', {
        'course': course,
        'activity': activity,
    })


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
