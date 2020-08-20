"""
Required by django
"""
from django import forms


class EnterWordsForm(forms.Form):
    words = forms.CharField(label='Words', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'pure-input-rounded'}), required=False)
