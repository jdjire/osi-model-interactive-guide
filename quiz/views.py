from django.shortcuts import render
from django.http import JsonResponse
from .models import Question

def quiz_view(request):
    return render(request, 'quiz.html')

def get_questions(_request):
    questions = Question.objects.all().order_by('?')[:10]  # Get 10 random questions
    data = []
    for q in questions:
        data.append({
            'id': q.id,
            'question': q.question,
            'option_a': q.option_a,
            'option_b': q.option_b,
            'option_c': q.option_c,
            'option_d': q.option_d,
            'correct_answer': q.correct_answer,
            'explanation': q.explanation,
        })
    return JsonResponse({'questions': data})
