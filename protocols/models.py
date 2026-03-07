from django.db import models
from osi.models import Layer

class Protocol(models.Model):
    name = models.CharField(max_length=50)
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE, related_name='protocol_details')
    default_port = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name
