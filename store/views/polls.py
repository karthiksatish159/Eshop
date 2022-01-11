from django.shortcuts import render
from django.views import View

from store.models import Question


class Poll(View):
    def get(self,request):
        latest_question_list = Question.objects.order_by('-pub_date')
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls.html', context)