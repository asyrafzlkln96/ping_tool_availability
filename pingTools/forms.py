# forms.py 

from django import forms
from .models import DataTerminals

class DataTerminalsCreate(forms.ModelForm):
    class Meta:
        model = DataTerminals
        fields = '__all__'