from django.http import Http404
from django.shortcuts import render
from django.views import View

from store.models import Question


class Detail(View):
    def get(self,request, question_id):
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request, 'detail.html', {'question': question})