from django import forms
from .models import Snap,Profile
from django.db import models
from django.contrib.auth.models import User





class PostForm(forms.ModelForm):
    class Meta:
        model = Snap
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profilepicture']
        # widgets = {
        #     'tags': forms.CheckboxSelectMultiple(),
        # }


# class VoteForm(forms.ModelForm):
#     class Meta:
#         model = Snap
#         fields = ['design','usability','content']

        