from django.shortcuts import render
from django.http import JsonResponse
from .models import Protocol

def protocol_explorer(request):
    protocols = Protocol.objects.select_related('layer').all()
    return render(request, 'protocol_explorer.html', {'protocols': protocols})

def get_protocols(request):
    layer_id = request.GET.get('layer_id')
    search_query = request.GET.get('search')
    
    protocols = Protocol.objects.select_related('layer').all()
    
    if layer_id:
        protocols = protocols.filter(layer__layer_number=layer_id)
        
    if search_query:
        protocols = protocols.filter(name__icontains=search_query)
        
    data = []
    for p in protocols:
        data.append({
            'name': p.name,
            'layer_name': p.layer.name if p.layer else 'Unknown',
            'default_port': p.default_port,
            'description': p.description,
        })
        
    return JsonResponse({'protocols': data})
