from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from .models import Layer, InterviewQuestion
import logging

logger = logging.getLogger(__name__)

def index(request):
    """Render the homepage."""
    try:
        layers = Layer.objects.all()
        logger.info(f"Found {layers.count()} layers")
        return render(request, 'index.html', {'layers': layers})
    except Exception as e:
        logger.error(f"Error in index view: {e}")
        # In production, return a simple error page
        if not settings.DEBUG:
            return render(request, 'error.html', {'error': 'Database error'}, status=500)
        raise

def layer_detail(_request, layer_number):
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
