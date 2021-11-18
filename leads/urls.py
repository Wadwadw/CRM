from django.urls import path
from .views import (
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
    AssignAgentView,
    CategoryListView,
    CategoryDetailView,
    LeadCategoryUpdateView
)

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='list-lead'),
    path('<int:pk>/', LeadDetailView.as_view(), name='detail-lead'),
    path('create/', LeadCreateView.as_view(), name='create-lead'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='update-lead'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='delete-lead'),
    path('<int:pk>/assign-agent/', AssignAgentView.as_view(), name='agent-assign'),
    path('<int:pk>/category-update/', LeadCategoryUpdateView.as_view(), name='category-update'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category-detail')
]
