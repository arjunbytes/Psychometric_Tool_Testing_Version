from django.db import models
from django.contrib.auth.models import User

class SurveyResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace 1 with your actual default user ID
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField()
    question5 = models.IntegerField()
    question6 = models.IntegerField()
    question7 = models.IntegerField()
    question8 = models.IntegerField()
    question9 = models.IntegerField()
    question10 = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}'s Survey Response"
