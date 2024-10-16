from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('contract-project/', views.contract_project, name='contract-project'),
    path('contract-detail/<int:pk>/', views.contract_project_detail, name='contract-detail'),
    path('contract-create/', views.contract_project_create, name='contract-create'),
    path('contract-update/<int:pk>/', views.contract_project_update, name='contract-update'),
    path('contract-delete/<int:pk>/', views.contract_project_delete, name='contract-delete'),
    path('create-ai-chat-contract/<int:contract_project_id>/', views.create_ai_chat_contract, name='create-ai-chat-contract'),
    path('get-chat-history-contract/<int:contract_project_id>/', views.get_chat_history_contract, name='get-chat-history-contract'),
]