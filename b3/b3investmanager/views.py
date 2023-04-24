from unittest import loader
from django.shortcuts import render

# Create your views here.
from django.http import Http404, HttpResponse
from .models import Code, Investment


def index(request):
    return HttpResponse('welcome to b3invest manager')


def code_index(request):
    codes = Code.objects.all()
    context = {"codes": codes}
    return render(request, "b3investmanager/code_index.html", context)


def investment_index(request):
    investments = Investment.objects.all()
    context = {"investments": investments}
    return render(request, "b3investmanager/investment_index.html", context)


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
