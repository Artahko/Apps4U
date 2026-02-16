from django.db.models import F
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
# from .models import Choice, Question

# Create your views here.
# class IndexView(generic.ListView):
#     template_name = "polls/index.html"
#     context_object_name = "latest_question_list"


def index(request):
    return render(request, "helper/index.html")

def activities(request):
    return HttpResponse("this is the activities page")
