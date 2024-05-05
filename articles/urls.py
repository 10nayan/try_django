from django.urls import path
from .views import article_detail_view, article_search_view, article_create_view

urlpatterns = [
    path('<int:id>', article_detail_view),
    path('', article_search_view),
    path('create', article_create_view),
]