from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.template import loader
from django.urls import reverse

# Create your views here.
def home(request):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  template = loader.get_template('polls/index.html')
  context = {
    'latest_question_list': latest_question_list
  }
  return HttpResponse(template.render(context, request))
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)

  # return HttpResponse("Hello, world. You've reached the polls page")

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/detail.html', {'question': question})
  # return HttpResponse("You're looking at question {}".format(question_id))

def results(request, question_id):
  return HttpResponse("You're looking at the results of question {}".format(question_id))

def vote(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render(request, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice."
    })
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id)))
  # return HttpResponse("You're voting in question {}".format(question_id))



