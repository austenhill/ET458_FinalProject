import imp
from django import forms
from django.forms import ModelForm
from importlib_metadata import requires
from .models import Quote

class QuoteForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Quote
        fields = [
            'name', 'phone', 'email', 'bio', 'major', 'classification', 'graduation', 
            'skills', 'languages', 'experience', 'picture'
        ]