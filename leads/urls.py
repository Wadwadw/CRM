from django.urls import path
from .views import lead_list, lead_detail, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', lead_list, name='list-lead'),
    path('<int:pk>/', lead_detail, name='detail-lead'),
    path('create/', lead_create, name='create-lead'),
    path('<int:pk>/update/', lead_update, name='update-lead'),
    path('<int:pk>/delete/', lead_delete, name='delete-lead')
]
