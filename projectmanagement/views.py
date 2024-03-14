from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Page d'accueil de l'Application de Gestion de Projet")
