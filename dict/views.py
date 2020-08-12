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
            json_returned = r.data.decode('utf-8')
            request.session["WORDS"] = json_returned
            # data.append(json.loads(r.data.decode('utf-8')))

        # print(data)
        # request.session["WORDS"] = data
    request.session.flush()
    word_form = EnterWordsForm(request.POST or None)
    context = {'form': word_form}

    if word_form.is_valid():
        get_words(word_form)
        return redirect("/words")

    return render(request, 'dict/home_screen.html', context)


def words_view(request):
    context = {}
    if request.session.has_key('WORDS'):
        data = request.session['WORDS']
        context = {'data' : data}
    return render(request, 'dict/words.html', context)
