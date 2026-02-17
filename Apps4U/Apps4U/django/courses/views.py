from django.shortcuts import render, get_object_or_404
from .models import Course, Activity

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/list.html', {'courses': courses})

def course_detail(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/detail.html', {'course': course})

def course_faq(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/faq.html', {'course': course})

def course_activities(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    return render(request, 'courses/activities.html', {'course': course})

def activity_detail(request, course_slug, activity_id):
    activity = get_object_or_404(
        Activity,
        id=activity_id,
        course__slug=course_slug
    )
    return render(request, "courses/detail_activity.html", {
        "activity": activity,
        "course": activity.course
    })
