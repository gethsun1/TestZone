from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Question, Choice


def base(request):
    latest_questions = Question.objects.order_by('post_date')[:5]
    # output = ','.join([i.question_text for i in latest_questions])
    context = {
        'latest_questions': latest_questions
    }
    return render(request, 'polls/base.html', context)


def detail(request, question_id):
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
        selected_choice += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    return HttpResponse(f'You are voting on question {question_id}')
