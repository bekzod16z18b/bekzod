from django.urls import path

from .views import (
    Artic3leListView,
    Artic3leUpdateView,
    Artic3leDeleteView,
    Artic3leDetailView,
    Artic3leCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', Artic3leUpdateView.as_view(), name="articles3_edit"),
    path('<int:pk>/', Artic3leDetailView.as_view(), name='articles3_detail'),
    path('<int:pk>/delete/', Artic3leDeleteView.as_view(), name='articles3_delete'),
    path('new/', Artic3leCreateView.as_view(), name='articles3_new'),
    path('', Artic3leListView.as_view(), name='articles3_list'),
]