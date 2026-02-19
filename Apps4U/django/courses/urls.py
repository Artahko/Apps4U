from django.urls import path
from . import views
# from .views import AddCommentView

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<slug:course_slug>/faq/', views.course_faq, name='course_faq'),
    path("<slug:course_slug>/activities/<int:activity_id>", views.activity_detail, name="activity_detail"),
    path("<slug:course_slug>/activities/<int:activity_id>/comment", views.add_comment, name="add_comment"),
    path("<slug:course_slug>/activities/", views.course_activities, name="course_activities"),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
]
