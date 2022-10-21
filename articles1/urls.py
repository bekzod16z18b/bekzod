from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="articles1_edit"),
    path('<int:pk>/', ArticleDetailView.as_view(), name='articles1_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles1_delete'),
    path('new/', ArticleCreateView.as_view(), name='articles1_new'),
    path('', ArticleListView.as_view(), name='articles1_list'),
]