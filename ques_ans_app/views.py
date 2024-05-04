from django.shortcuts import render, redirect
from .models import Question, UserResponse, TestResult


def start_test(request):
    TestResult.objects.filter(user=request.user).delete()
    start_question_id = 4
    return redirect('ques_ans_app:question', question_id=start_question_id)


def question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        selected_choice_id = request.POST['choice']
        selected_choice = question.choice_set.get(pk=selected_choice_id)
        user_response = UserResponse.objects.create(user=request.user,
                                                    choice=selected_choice)
        test_result, created = TestResult.objects.get_or_create(
            user=request.user
        )
        test_result.responses.add(user_response)
        next_question = selected_choice.next_question
        if next_question:
            return redirect('ques_ans_app:question',
                            question_id=next_question.id)
        else:
            return redirect('ques_ans_app:finish_test')
    return render(request, 'question.html', {'question': question})


def finish_test(request):
    test_result = TestResult.objects.filter(user=request.user).last()
    if test_result:
        user_responses = test_result.responses.all()
        user_responses = user_responses.filter(user=request.user,
                                               testresult=test_result)
    else:
        user_responses = []
    return render(request,
                  'finish_test.html',
                  {'user_responses': user_responses})
