# news/forms.py
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

class NewsSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
    
