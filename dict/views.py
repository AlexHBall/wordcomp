from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers

from .forms import EnterWordsForm

import urllib3
import json

# Create your views here.


def home_view(request):
    def get_words(form):
        words = [form.cleaned_data['first_word'],
                 form.cleaned_data['second_word']]
        http = urllib3.PoolManager()
        base_url = "https://api.dictionaryapi.dev/api/v1/entries/fr/"
        urls = []
        for word in words:
            urls.append(base_url+word)
        data = []
        for url in urls:
            r = http.request('GET', url)
            data.append(json.loads(r.data.decode('utf-8')))

        
        request.session["WORDS"] = serializers.serialize(data)

    word_form = EnterWordsForm(request.POST or None)
    context = {'form': word_form}

    if word_form.is_valid():
        get_words(word_form)
        return redirect("/words")

    return render(request, 'dict/home_screen.html', context)


def words_view(request):
    def get_words():
        words=[]
        words_from_session = serializers.deserialize(
            "json", request.session.get("WORDS"))

        for word in words_from_session:
            words.append(word.object)

        return words
    words = get_words()
    print(words)
    return render(request, 'dict/words.html', {})
