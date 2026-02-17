from django.shortcuts import render, get_object_or_404
from .models import Course, Activity, Comment
from django.views.generic.edit import CreateView
from .forms import CommentForm
from django.urls import reverse


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
    return render(request, 'activities/activities.html', {'course': course})


def activity_detail(request, course_slug, activity_id):
    activity = get_object_or_404(
        Activity,
        id=activity_id,
        course__slug=course_slug
    )
    return render(request, "activities/detail_activity.html", {
        "activity": activity,
        "course": activity.course
    })


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "activities/add_comment.html"
    # fields = "__all__"
    def form_valid(self, form):
        activity = get_object_or_404(
            Activity,
            id=self.kwargs['activity_id']
        )

        form.instance.post = activity   # THIS FIXES THE ERROR
        return super().form_valid(form)

    def get_success_url(self):
        course_slug = self.kwargs['course_slug']
        activity_id = self.kwargs['activity_id']
        # Reverse the URL dynamically
        return reverse(
                'activity_detail',
                kwargs={
                    'course_slug': self.kwargs['course_slug'],
                    'activity_id': self.kwargs['activity_id'],
                }
            )
