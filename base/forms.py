from django import forms

from .models import URLMapping

class URLForm(forms.ModelForm):

    class Meta:
        model = URLMapping
        fields = '__all__'
