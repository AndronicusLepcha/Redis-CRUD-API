from django import forms
from django import forms
from .models import dummy_model_data


class dummy_data_form(forms.ModelForm):
    class Meta:
        model = dummy_model_data
        fields = ['file_name','created_by','file_type','file_size','file','description','is_public','file_extension','tags','is_archived','category']
