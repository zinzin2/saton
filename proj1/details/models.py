from django.db import models

# Create your models here.

class Details (models.Model):
    objects = models.Manager()
    title =  models.CharField(max_length=200)
    user_name = models.CharField(max_length=50, null=True)
    user_num = models.IntegerField() 
    content = models.TextField(blank=True, null=True)
    post_type = models.IntegerField(default=1)

    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)