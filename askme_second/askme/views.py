from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index (request):
    context = {'questions': QUESTIONS}
    #return render(request, 'index.html', context)


def question(request, question_id):
    context = {'question': models.QUESTIONS[question_id]}
    return render(request, 'question.html', context)