"""
Required by django
"""
from django import forms

class EnterWordsForm(forms.Form):
    first_word = forms.CharField(label='First Word', max_length=100)
    second_word = forms.CharField(label='Second Word', max_length=100)
