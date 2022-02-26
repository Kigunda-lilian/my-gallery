from logging import PlaceHolder
from django import forms
from .models import categories

class search_form(forms.Forms):
    category=forms.ModelChoiceField(queryset=categories.objects.all(),widget=forms.Select(attrs={"PlaceHolder":"category"}))