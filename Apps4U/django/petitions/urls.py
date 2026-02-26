from django.urls import path
from . import views

urlpatterns = [
    path('', views.faq_list, name='faq_list'),

    path('<int:question_id>/', views.faq_detail, name='faq_detail'),
    path('<int:question_id>/comment', views.add_answer, name='add_answer'),

]
