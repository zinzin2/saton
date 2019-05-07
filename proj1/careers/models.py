from django.db import models

# Create your models here.

class Careers (models.Model):
    content = models.TextField(blank=True, null=True)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

