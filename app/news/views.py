"""Views"""


from django.shortcuts import render
from django.conf import settings
from news.models import News


# Create your views here.
def index(request):
    context = {
        "news": News.objects.all()
    }
    return render(request, "news/index.html", context)


def info(request):
    context = {
        "news_count": News.objects.all().count(),
        "site_version": settings.SITE_VERSION
    }
    return render(request, "news/info.html", context)
