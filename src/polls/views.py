from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("Hello, world. You've reached the polls page")

def detail(request, question_id):
  return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
  return HttpResponse("You're looking at the results of question {}".format(question_id))

def vote(request, question_id):
  return HttpResponse("You're voting in question {}".format(question_id))



