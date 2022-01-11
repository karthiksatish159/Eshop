from django.views import View
from django.shortcuts import get_object_or_404, render

from store.models import Question


class Results(View):
    def get(self,request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'results.html', {'question': question})