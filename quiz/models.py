from django.db import models
from osi.models import Layer

class Question(models.Model):
    ANSWER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ]
    
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=1, choices=ANSWER_CHOICES)
    explanation = models.TextField()
    layer_reference = models.ForeignKey(Layer, on_delete=models.CASCADE, related_name='questions', null=True, blank=True)

    def __str__(self):
        return self.question[:50]
