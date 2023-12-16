from django.urls import path
from page_app.views import index, contato, services

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),
    path('services/', services),
    path('contato/', contato),
]