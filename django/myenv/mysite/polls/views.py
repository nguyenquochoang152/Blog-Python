from django.shortcuts import render

# Create your views here.
from django.template import loader

from .models import Question
from django.http import HttpResponse


def index(request):

    #return HttpResponse("Hello, world. You're at the polls index.")
    name ="Hoang"
    group_name=["Lan","Mai","Dao"]
    context = {'my_name':name}
    context["group_name"]=group_name
    return render(request, 'polls/index.html', context,group_name)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)