from django.shortcuts import render

from .models import Question, Choice

# Get Questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html')
