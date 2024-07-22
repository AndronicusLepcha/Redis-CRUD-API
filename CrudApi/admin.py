from django.contrib import admin
from .models import dummy_model_data
# Register your models here.
myModels = [dummy_model_data]
admin.site.register(myModels)