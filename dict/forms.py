"""
Required by django
"""
from django import forms


class EnterWordsForm(forms.Form):
    # words = forms.CharField(label='', max_length=100,
    #                         widget=forms.CharField(attrs={'class': 'words-input'}))

    words = forms.CharField(label='Words', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'words-input'}), required=False)
    to_search = forms.CharField(widget=forms.HiddenInput(
        attrs={'class': 'words-hidden'}), required=False)
