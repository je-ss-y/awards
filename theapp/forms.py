from django import forms
from .models import Snap





class PostForm(forms.ModelForm):
    class Meta:
        model = Snap
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }