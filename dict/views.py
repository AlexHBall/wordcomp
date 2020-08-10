from django.shortcuts import render, HttpResponse
import urllib3
import json

# Create your views here.


def home_view(request):
    http = urllib3.PoolManager()
    base_url = "https://api.dictionaryapi.dev/api/v1/entries/fr/"
    word = "étoile"
    url = base_url + word
    r = http.request('GET', url)
    data = json.loads(r.data.decode('utf-8'))
    html = "<html><body><pre>Data: %s.</pre></body></html>" % json.dumps(
        data, indent=2)
    return render(request, 'dict/home_screen.html', {})
