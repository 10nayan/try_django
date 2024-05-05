from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id:
        article_obj = Article.objects.get(id=id)
    context= {'object': article_obj}
    return render(request, 'articles/article-detail.html', context=context)

