from django.http import HttpResponse
from articles.models import Article
import random

RANDOM_ID = random.randint(1, 3)

def home_view(request):
    random_obj = Article.objects.get(id=RANDOM_ID)
    html_string = f"""
    <h1>Hello World</h1>
    <p>Title: {random_obj.title}</p>
    <p>Content: {random_obj.content}</p>
    """
    return HttpResponse(html_string)