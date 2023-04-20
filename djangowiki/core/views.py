from django.shortcuts import render

from wiki.models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'core/index.html', {'articles': articles})
