from django.db import models
from django.utils import timezone

class Anotacao(models.Model):
    STATUS_CHOICES = [
        ('todo', 'A Fazer'),
        ('done', 'Concluída'),
    ]
      
    titulo = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    data = models.DateField(default=timezone.now)
