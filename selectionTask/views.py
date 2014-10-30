from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from models import Subject, Question, Result
import os
import json


def home(request):
    with open(os.path.join(os.path.dirname(__file__), "../static/index.html"), 'r') as index_html_file:
        return HttpResponse(index_html_file.read(), content_type='text/html')


@csrf_exempt
def load_questions(request):
    if not 'id' in request.POST:
        return HttpResponse('{"Error": "No ID supplied."}', content_type='application/json', status=400)
    try:
        subject = Subject.objects.filter(subject_id=request.POST['id']).all()[0]
    except IndexError:
        subject = Subject(subject_id=request.POST['id'], age=42, gender="male")
        subject.save()
    if subject.results.count() >= Question.objects.count():
        return HttpResponse('{"Error": "All question already answered. If you came you came to this from the pre-treatment, '
                            'please contact your survey company"}', content_type='application/json')
    quest = Question.objects.all()[subject.results.count()]
    return HttpResponse(json.dumps({
        'question_id': quest.pk,
        'person': quest.person,
        'question': quest.question,
        'image': quest.image_url,
        'progress': subject.results.count()
    }), content_type='application/json')