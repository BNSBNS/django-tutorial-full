import datetime

from django.db import models
from django.utils import timezone


# NOTES ABOUT __STR__
# Most notably, to display an object in the Django admin site and as the value inserted into a template when it displays an object. 
# Thus, you should always return a nice, human-readable representation of the model from the __str__() method.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text