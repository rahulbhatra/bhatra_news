from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.
# Init
headers = [
    {'title': 'News', 'url': ''},
    {'title': 'Sports', 'url': ''},
    {'title': 'Login', 'url': '/login'},
   ]
def Index(request):
    newsapi = NewsApiClient(api_key='a9d28d61c1fa4d44aa4a47bc6814b4d9')
    top_headlines = newsapi.get_top_headlines(sources='bbc-news,the-verge')
    all_articles = top_headlines['articles']
    return render(request, 'index.html', context={'headlines': top_headlines,
                                                  'articles': all_articles,
                                                  'headers': headers})
