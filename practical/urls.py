from django.urls import path

from .views import (
    PracticalListView,
    PracticalUpdateView,
    PracticalDeleteView,
    PracticalDetailView,
    PracticalCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/', PracticalUpdateView.as_view(), name="practical_edit"),
    path('<int:pk>/', PracticalDetailView.as_view(), name='practical_detail'),
    path('<int:pk>/delete/', PracticalDeleteView.as_view(), name='practical_delete'),
    path('new/', PracticalCreateView.as_view(), name='practical_new'),
    path('', PracticalListView.as_view(), name='practical_list'),
]