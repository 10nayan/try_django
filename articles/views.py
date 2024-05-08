from django.shortcuts import render
from .models import Article
from .forms import ArticleForm, ArticleModelForm
from django.contrib.auth.decorators import login_required

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

@login_required
def article_create_view(request):
    form = ArticleModelForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleModelForm

    return render(request, 'articles/article-create.html', context=context)

