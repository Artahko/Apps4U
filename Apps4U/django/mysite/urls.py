from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<slug:course_slug>/', views.course_detail, name='course_detail'),
    path('<slug:course_slug>/faq/', views.course_faq, name='course_faq'),
    path("<slug:course_slug>/activities/", views.course_activities, name="course_activities"),
    path("accounts/", include("allauth.urls"))
    path('admin/', admin.site.urls),
    path('', include('courses.urls')),
]

