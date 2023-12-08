from django.urls import path
from page_app.views import index, contato, footer, header, services, welcome

urlpatterns = [
    # Cadastrar URLs aqui
    path('', index),

    path('contato/', contato),

    path('footer/', footer),

    path('header/', header),

    path('services/', services),

    path('welcome/', welcome), 
]