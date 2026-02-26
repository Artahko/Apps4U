from django.shortcuts import render, redirect, get_object_or_404
from .models import Petition, Vote
from django.db.models import Exists, OuterRef, Count, Sum
from django.utils import timezone
from datetime import timedelta
# from .forms import QuestionForm, AnswerForm

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
# Create your views here.



@login_required
def petition_list(request):
    cutoff_date = timezone.now() - timedelta(days=30)

    user_votes = Vote.objects.filter(petition=OuterRef('pk'), user=request.user)

    petitions = Petition.objects.filter(
        created_at__gte=cutoff_date
    ).annotate(
        user_has_voted=Exists(user_votes),
        vote_count=Count('votes')
    ).order_by('-created_at')

    return render(request, 'petition_list.html', {
        'petitions': petitions,
    })


@login_required
def make_petition(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')


        if title and content:
            Petition.objects.create(
                user=request.user,
                title=title,
                content=content
            )
    return redirect('petition_list')


@login_required
def vote_petition(request, petition_id):
    petition = get_object_or_404(Petition, id=petition_id)

    vote_qs = Vote.objects.filter(user=request.user, petition=petition)

    if vote_qs.exists():
        vote_qs.delete()
        action = "unvoted"
    else:
        Vote.objects.create(user=request.user, petition=petition, value=1)
        action = "voted"

    from django.db.models import Count
    count = petition.votes.count()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'action': action, 'count': count})

    return redirect('petition_list')
