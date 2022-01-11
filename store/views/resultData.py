from django.views import View
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from store.models import Question


class ResultData(View):
    def get(self,request, obj):
        votedata = []

        question = Question.objects.get(id=obj)
        votes = question.choice_set.all()

        for i in votes:
            votedata.append({i.choice_text: i.votes})

        print(votedata)
        return JsonResponse(votedata, safe=False)