from django.db import models


class Question (models.Model):
    person = models.CharField(max_length=30)
    question = models.TextField()
    correct_answer = models.CharField(max_length=5)
    image_url = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Question: ' + str(self.id)


class Subject (models.Model):
    subject_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()

    def __unicode__(self):
        return 'Subject: ' + self.subject_id


class Result (models.Model):
    answer_is_correct = models.BooleanField()
    answer_time = models.FloatField()
    subject = models.ForeignKey(Subject, related_name='results')

    def __unicode__(self):
        return 'Result No. ' + str(self.id) + ' of ' + str(self.subject)
