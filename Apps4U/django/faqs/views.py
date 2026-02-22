from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse


@login_required
def faq_list(request):
    questions = Question.objects.all().order_by('-created_at')
    courses = Course.objects.all() # Fetch courses for the dropdown
    return render(request, 'faq_list.html', {
        'questions': questions,
        'courses': courses
    })

@login_required
def faq_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('faq_detail', question_id=question.id)
    else:
        form = AnswerForm()
    return render(request, 'faq_detail.html', {'question': question, 'form': form})

@login_required
def ask_question(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        course_id = request.POST.get('course_id')

        if title and content and course_id:
            course = Course.objects.get(id=course_id)
            Question.objects.create(
                user=request.user,
                course=course,
                title=title,
                content=content
            )
    return redirect('faq_list')



def get_answers(request, question_id):
    answers = Answer.objects.filter(question_id=question_id).order_by('created_at')
    data = [{"user": a.user.username, "text": a.text, "date": a.created_at.strftime("%H:%M")} for a in answers]
    return JsonResponse(data, safe=False)

@login_required
def post_answer(request, question_id):
    if request.method == "POST":
        text = request.POST.get('text')
        question = get_object_or_404(Question, id=question_id)
        if text:
            Answer.objects.create(
                user=request.user,
                question=question,
                text=text
            )
            # Return a 200 OK status to let JavaScript know it can redirect
            return HttpResponse(status=200)
    return HttpResponse(status=400)
