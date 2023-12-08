from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,"page_app/partial/home.html")

def contato (request):
    return render(request, "page_app/partial/contato.html")

def footer (request):
    return render(request, "page_app/partial/footer.html")

def header (request):
    return render(request, "page_app/partial/header.html")

def services (request):
    return render(request, "page_app/partial/services.html")

def welcome (request):
    return render(request, "page_app/partial/welcome.html")