from django.db import models

# Create your models here.

from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()