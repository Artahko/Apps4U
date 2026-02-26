from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from courses.models import Course
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse


@login_required
def faq_list(request):
    questions = Question.objects.all().order_by('-created_at')
    courses = Course.objects.all()
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


@login_required
def add_answer(request, question_id):
    question_obj = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)

            answer.question = question_obj

            if request.user.is_authenticated:
                answer.user = request.user
            else:

                return redirect('login')

            answer.save()
            return redirect('faq_detail', question_id=question_obj.id)
    else:
        form = AnswerForm()

    return render(request, 'add_answer.html', {'form': form, 'question': question_obj})
