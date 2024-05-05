from django.shortcuts import render
from .models import Article

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id:
        article_obj = Article.objects.get(id=id)
    context= {'object': article_obj}
    return render(request, 'articles/article-detail.html', context=context)

def article_search_view(request):
    article_obj = None
    query_dict = request.GET
    query = query_dict.get('q')
    if query:
        article_obj = Article.objects.get(id=query)
    context= {'object': article_obj}
    return render(request, 'articles/article-search.html', context=context)

def article_create_view(request):
    context = {}
    if request.method == "POST":
        query_dict = request.POST
        title = query_dict.get('title')
        content = query_dict.get('content')
        article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request, 'articles/article-create.html', context=context)

