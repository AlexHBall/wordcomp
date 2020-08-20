from django.shortcuts import render, HttpResponse, redirect
from django.core import serializers

from .forms import EnterWordsForm
from .models import Word
import urllib3
import json
# Create your views here.


def home_view(request):
    def get_words(form):
        form_data = form.cleaned_data['words']
        words = form_data.split(" ")
        http = urllib3.PoolManager()
        base_url = "https://api.dictionaryapi.dev/api/v1/entries/fr/"
        urls = []
        for word in words:
            urls.append(base_url+word)
        data = []
        for url in urls:
            r = http.request('GET', url)
            json_returned = json.loads(r.data.decode('utf-8'))
            data.append(json_returned)

        request.session["WORDS"] = data
    request.session.flush()
    word_form = EnterWordsForm(request.POST or None)
    context = {'form': word_form}

    if word_form.is_valid():
        get_words(word_form)
        return redirect("/words")

    return render(request, 'dict/home_screen.html', context)


def words_view(request):
    if request.session.has_key('WORDS'):
        data = request.session['WORDS']
        jsons = []
        for d in data:
            jsons.append(d)

    words = [Word(j[0]) for j in jsons]

    context = {
        'words' : [w.return_dict() for w in words]
    }
    return render(request, 'dict/words.html', context)
