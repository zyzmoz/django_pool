from django.shortcuts import render
from django.http import HttpResponse
from .models import Question

# Create your views here.
def home(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  output = ', '.join([q.question_text for q in latest_question_list])
  return HttpResponse(output)

  # return HttpResponse("Hello, world. You've reached the polls page")

def detail(request, question_id):
  return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
  return HttpResponse("You're looking at the results of question {}".format(question_id))

def vote(request, question_id):
  return HttpResponse("You're voting in question {}".format(question_id))



