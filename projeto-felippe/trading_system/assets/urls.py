from django.urls import path
from . import views

# Define as rotas da aplicação
urlpatterns = [
    path('', views.index, name='index'),  # Rota para a página inicial
    path('update_quotations/', views.update_quotations, name='update_quotations'),  # Rota para atualizar as cotações
]

