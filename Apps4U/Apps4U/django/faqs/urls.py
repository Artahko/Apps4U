from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list, name='faq_list'),
    path('ask/', views.ask_question, name='ask_question'),
    path('<int:question_id>/', views.faq_detail, name='faq_detail'),
    path('api/answers/<int:question_id>/', views.get_answers, name='get_answers'),
    path('answer/<int:question_id>/', views.post_answer, name='post_answer'),
]
