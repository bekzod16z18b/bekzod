from django.urls import path

from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="articles4_edit"),
    path('<int:pk>/', ArticleDetailView.as_view(), name='articles4_detail'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='articles4_delete'),
    path('new/', ArticleCreateView.as_view(), name='articles4_new'),
    path('', ArticleListView.as_view(), name='articles4_list'),
]