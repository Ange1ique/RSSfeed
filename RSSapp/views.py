from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
import datetime
from .models import RSS_URLS
from .forms import InputURLS
import feedparser


# Create your views here.
def Index(request):
    now = datetime.datetime.now()
    str_now = now.strftime("%d %B, %Y")

    if request.method == 'POST':
        url1 = request.POST['url1']
        url2 = request.POST['url2']
        url3 = request.POST['url3']
        urls = [url1, url2, url3]
        titles = []
        feeds = []
        for url in urls:
            if not url:
                pass
            else:
                if 'www' in url:
                    i1 = url.find('.')
                    i2 = url.find('.', (i1+1))
                    titles.append(url[(i1+1):i2])
                else:
                    i1 = 2 + url.find('/')
                    i2 = url.find('.')
                    titles.append(url[i1:i2])
                if feedparser.parse(url):
                    feeds.append(feedparser.parse(url))
                else:
                    feeds.append("No RSS feeds found for the given url")

        context = {"titles": titles, "feeds": feeds, "date": str_now}
        return render(request, 'results.html', context)

    else:
        form = InputURLS()
        context = {"form": form,"date": str_now}
        return render(request, 'index.html', context)


def Results(request):
    return render(request, 'results.html')
