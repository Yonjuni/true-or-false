from django.db import models


class Question (models.Model):
    person = models.CharField(max_length=30)
    question = models.TextField()
    correct_answer = models.CharField(max_length=5)
    image_url = models.CharField(max_length=50)


class Subject (models.Model):
    gender = models.CharField(max_length=6)
    age = models.IntegerField()


class Result (models.Model):
    answer_is_correct = models.BooleanField()
    answer_time = models.FloatField()
    subject = models.ForeignKey(Subject, related_name='results')