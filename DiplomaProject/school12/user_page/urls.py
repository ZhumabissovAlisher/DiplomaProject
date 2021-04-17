from django.urls import path
from user_page import views

urlpatterns = [
    path('',views.main,name = "main"),
    path('news/<int:pk>/',views.news_special,name = 'news_special'),
    path('student/',views.student,name = "student"),
    path('teacher/',views.teacher,name = "teacher"),
    path('course/',views.course,name = "course"),
    path('programming/',views.programming,name = "programming"),
    path('ent/',views.ent,name = "ent"),
    path('sport/',views.sport,name = "sport"),
    path('technology/',views.technology,name = "technology"),
    path('art/',views.art,name = "art"),
]
