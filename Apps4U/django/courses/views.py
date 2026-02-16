from django.shortcuts import render, get_object_or_404
from .models import Course

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
