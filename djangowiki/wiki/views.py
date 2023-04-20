from random import randint

from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import Article
from .forms import CreateArticleForm, EditArticleForm


def random_article(request):
    articles = Article.objects.all()
    random_index = randint(0, len(articles)-1)
    article = list(articles)[random_index]
    return render(request, 'wiki/view_article.html', {"article": article})


def view_article(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'wiki/view_article.html', {"article": article})


def create_article(request):
    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("wiki:view_article", slug=article.slug)
    else:
        form = CreateArticleForm()
    return render(request, "wiki/form.html", {
        "form": form,
        "title": "Create article"
    })


def edit_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = EditArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("wiki:view_article", slug=article.slug)
    else:
        form = EditArticleForm(instance=article)
    return render(request, "wiki/form.html", {
        "form": form,
        "title": f"Edit {article.title}"
    })


def delete_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated and request.user.is_staff:
        article.delete()
    return redirect("core:index")


def search(request):
    query = request.GET.get("q")
    articles = Article.objects.filter(Q(title__icontains=query) | Q(content__icontains=query) | \
                                    Q(created_on__icontains=query) | Q(updated_on__icontains=query))
    return render(request, "wiki/search.html", {'query': query, 'articles': articles})
