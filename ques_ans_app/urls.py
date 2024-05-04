from django.urls import path
from . import views

app_name = 'ques_ans_app'

urlpatterns = [
    path('', views.start_test, name='start_test'),
    path('question/<int:question_id>/', views.question, name='question'),
    path('finish/', views.finish_test, name='finish_test'),
]
