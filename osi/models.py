from django.db import models

class Layer(models.Model):
    layer_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    real_life_example = models.TextField()
    protocols = models.TextField()

    class Meta:
        ordering = ['-layer_number']

    def __str__(self):
        return f"Layer {self.layer_number}: {self.name}"

class InterviewQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    
    def __str__(self):
        return self.question[:50]
