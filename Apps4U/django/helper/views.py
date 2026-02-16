from django.db.models import F
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from .models import Activity
# from .models import Choice, Question

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"


def index(request):
    return render(request, "helper/index.html")

# def activities(request):
#     return HttpResponse("this is the activities page")

def activities_list(request):
    activities = Activity.objects.all()
    return render(request, "activities/list.html", {
        "activities": activities
    })


def activity_detail(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    return render(request, "activities/detail.html", {
        "activity": activity
    })
