from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    next_question = models.ForeignKey(Question,
                                      on_delete=models.CASCADE,
                                      related_name='next',
                                      blank=True,
                                      null=True)

    def __str__(self):
        return self.choice_text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey('Choice', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s response: {self.choice.choice_text}"


class TestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    responses = models.ManyToManyField(UserResponse)

    def __str__(self):
        return f"Test result for {self.user.username}"
