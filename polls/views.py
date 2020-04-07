from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class BaseView(generic.ListView):
    template_name = 'polls/base.html'
    context_object_name = 'latest_question'

    def get_queryset(self):
        return Question.objects.order_by('-post_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    context_object_name = 'question'
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You Did Not Select Any Choice"
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))
