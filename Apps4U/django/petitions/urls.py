from django.urls import path
from . import views

urlpatterns = [
    path('', views.petition_list, name='petition_list'),
    path('make/', views.make_petition, name='make_petition'),
    path('<int:petition_id>/vote/', views.vote_petition, name='vote_petition'),


]
