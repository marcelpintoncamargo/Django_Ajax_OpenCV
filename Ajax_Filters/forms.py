from django import forms
from .models import  SaveImageModel

class SaveImageForm(forms.ModelForm):
    class Meta:
        model = SaveImageModel
        fields = ('image', 'name', 'description', )