from django.http import Http404
from django.shortcuts import render

# Create your views here.
from .models import *


def home(request):
    try:
        articles = Articles.objects.filter().order_by('-id')[:5]

    except:
        articles = None
    print(articles)
    context = {
        "article": articles,
    }
    return render(request, "articles/index.html", context=context)


def blog(request):
    return render(request, "articles/blog.html")


def blog_view(request, slug=None):
    article_obj = None
    if slug is not None:
        article_obj = Articles.objects.get(slug=slug)
        try:
            article_obj = Articles.objects.get(slug=slug)
        except Articles.DoesNotExist:
            raise Http404
        except:
            raise Http404

    context = {
        "object": article_obj
    }

    return render(request, 'articles/blog_details.html', context=context)


def about(request):
    return render(request, "articles/about.html")
