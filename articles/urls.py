from django.urls import path
from .views import article_detail_view

urlpatterns = [
    path('<int:id>', article_detail_view)
]