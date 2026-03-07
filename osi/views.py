from django.shortcuts import render
from django.http import JsonResponse
from .models import Layer, InterviewQuestion

def index(request):
    """Render the homepage."""
    layers = Layer.objects.all()
    return render(request, 'index.html', {'layers': layers})

def layer_detail(request, layer_number):
    """API endpoint to fetch layer details safely via AJAX."""
    try:
        layer = Layer.objects.get(layer_number=layer_number)
        data = {
            'layer_number': layer.layer_number,
            'name': layer.name,
            'description': layer.description,
            'real_life_example': layer.real_life_example,
            'protocols': layer.protocols,
        }
        return JsonResponse(data)
    except Layer.DoesNotExist:
        return JsonResponse({'error': 'Layer not found'}, status=404)

def comparison(request):
    return render(request, 'comparison.html')

def simulation(request):
    return render(request, 'packet_simulation.html')

def interview(request):
    questions = InterviewQuestion.objects.all()
    return render(request, 'interview.html', {'questions': questions})
