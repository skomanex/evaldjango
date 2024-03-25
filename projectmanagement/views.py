from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from projectmanagement.models import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Utilisateur.objects.get(mail = email, mdp = password)
            return redirect(reverse('pageutilisateur', args = [user.nom]))
        except Utilisateur.DoesNotExist:
            return render(request, 'login.html', {'error': 'Mauvais mail ou mot de passe'})             
    return render(request, "login.html")

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
        return render(request, "pageutilisateur.html", data)
    
    except Utilisateur.DoesNotExist:
        return render(request, "pageutilisateur.html", {'error' : 'Utilisateur introuvable'})