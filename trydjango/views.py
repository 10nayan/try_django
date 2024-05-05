from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random

RANDOM_ID = random.randint(1, 2)

def home_view(request):
    random_obj = Article.objects.get(id=RANDOM_ID)
    article_queryset = Article.objects.all()
    context = {
        'articles': article_queryset,
        'id': random_obj.id,
        'title': random_obj.title,
        'content': random_obj.content
    }
    html_string = render_to_string("home-view.html", context=context)
    return HttpResponse(html_string)