from django.http import HttpResponse, JsonResponse
from projectmanagement.models import *

# Create your views here.
def index(request):
    return HttpResponse("Page d'accueil de l'Application de Gestion de Projet")

def pageutilisateur(request, utilisateur):
    try: 
        user = Utilisateur.objects.get(nom = utilisateur)
        projects = Projet.objects.filter(responsable__id = user.id)
        tasks = Tache.objects.filter(executant__id = user.id)

        for project in projects:
            try:
                earliest = Tache.objects.filter(projet_id = project.id).order_by('dateDebut')[0]
                project.dateDebut = earliest.dateDebut
                latest = Tache.objects.filter(projet_id = project.id).order_by('-dateFin')[0]
                project.dateLivraison = latest.dateFin
            except IndexError:
                project.dateDebut = None
                project.dateLivraison = None

        data = {
            'utilisateur': user.to_json(),
            'projects': [project.to_json() for project in projects],
            'tasks': [task.to_json() for task in tasks]
        }
        return JsonResponse(data)
    
    except Utilisateur.DoesNotExist:
        return JsonResponse({'erreur': 'Utilisateur non trouvé'}, status = 404)