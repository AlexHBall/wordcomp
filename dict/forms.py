"""
Required by django
"""
from django import forms

class EnterWordsForm(forms.Form):
    words = forms.CharField(label='Enter words to compare', max_length=100)
