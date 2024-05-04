from django.shortcuts import render, redirect
from .models import Question

def start_test(request):
    start_question_id = 4
    return redirect('ques_ans_app:question', question_id=start_question_id)

def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        selected_choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=selected_choice_id)
        next_question = selected_choice.next_question
        if next_question:
            return redirect('ques_ans_app:question', question_id=next_question.id)
        else:
            return redirect('ques_ans_app:finish_test')
    return render(request, 'question.html', {'question': question})

def finish_test(request):
    return render(request, 'finish_test.html')
