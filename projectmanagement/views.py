from django.http import JsonResponse, Http404
from django.utils import timezone
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

            # Création de la session de login
            # request.session['pp_login'] = True
            return redirect(reverse('pageutilisateur', args = [user.nom]))
        except Utilisateur.DoesNotExist:
            return render(request, 'login.html', {'error': 'Mauvais mail ou mot de passe'})             
    return render(request, "login.html")

def pageutilisateur(request, utilisateur):
    # if 'pp_login' in request.session:
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
                    project.statut = 4

            data = {
                'utilisateur': user.to_json(),
                'projects': [project.to_json() for project in projects],
                'tasks': [task.to_json() for task in tasks]
            }

            # Suppression de la session de login
            # del request.session['pp_login']
            return render(request, "pageutilisateur.html", data)
        
        # Artefact datant d'avant le login, puisque le login vérifie déjà l'existance en BDD de l'utilisateur le try except est redondant.
        except Utilisateur.DoesNotExist:
            return render(request, "pageutilisateur.html", {'error' : 'Utilisateur introuvable'})
    # else :
        raise Http404