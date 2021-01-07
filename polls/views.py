from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from django.template import loader      # !!!
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
    question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
    raise Http404("진행 중인 투표가 없습니다.")
    return render(request, 'polls/detail.html', {'question': question})
    def detail(request, question_id):
    return HttpResponse("%s번 투표 상세 보기" % question_id)


def results(request,question_id):
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("질문에 투표해주세요 %s." % question_id)
