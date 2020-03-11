from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.views import generic
from django.urls import reverse

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'
  
  def get_queryset(self):
    """Return the last five published questions."""
    return Question.objects.order_by('-pub_date')[:5]
  # latest_question_list = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # context = {
  #   'latest_question_list': latest_question_list
  # }
  # return HttpResponse(template.render(context, request))
  # output = ', '.join([q.question_text for q in latest_question_list])
  # return HttpResponse(output)

  # return HttpResponse("Hello, world. You've reached the polls page")

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'
  # question = get_object_or_404(Question, pk=question_id)
  # return render(request, 'polls/detail.html', {'question': question})
  # return HttpResponse("You're looking at question {}".format(question_id))

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'
  # question = get_object_or_404(Question, pk=question_id)
  # return render(request, 'polls/results.html', {'question': question})

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
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
  # return HttpResponse("You're voting in question {}".format(question_id))


  



