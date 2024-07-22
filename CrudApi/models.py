from django.db import models

# Create your models here.
from django.db import models

class dummy_model_data(models.Model):
    
    file_name = models.CharField(blank=True,max_length=20)
    created_by = models.CharField(blank=True,max_length=20)
    file_type = models.CharField(blank=True,max_length=20)
    file_size = models.IntegerField(null=True)
    
    file = models.FileField(upload_to='uploads/')
    
    description = models.TextField(null=True,blank=True) 
    is_public = models.BooleanField(default=False)  
  
    file_extension = models.CharField(blank=True,max_length=10)
    tags = models.CharField(max_length=100, blank=True)
    is_archived = models.BooleanField(default=False)
    category = models.CharField(max_length=50, blank=True)