from django.http import JsonResponse, Http404
from django.utils import timezone
from django.shortcuts import render, redirect
from django.urls import reverse
from projectmanagement.models import *
from projectmanagement.forms import *

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Utilisateur.objects.get(mail=email, mdp=password)

            # Stockez l'utilisateur connecté dans la session
            request.session['user_id'] = user.id

            # Création de la session de login
            # request.session['pp_login'] = True
            return redirect(reverse('pageutilisateur', args=[user.nom]))
        except Utilisateur.DoesNotExist:
            error = 'Mauvais mail ou mot de passe'
            return render(request, 'login.html', {'error': error})
    return render(request, "login.html")


def pageutilisateur(request, utilisateur):
    # if 'pp_login' in request.session:
        try: 
            user = Utilisateur.objects.get(nom = utilisateur)
            projects = Projet.objects.filter(responsable__id = user.id)
            tasks = Tache.objects.filter(executant__id = user.id)

            for project in projects:
                try:
                    # Associe les dates de début et de fin de projet en fonction des date de debut et de fin des tâches
                    earliest = Tache.objects.filter(projet_id = project.id).order_by('dateDebut')[0]
                    project.dateDebut = earliest.dateDebut
                    latest = Tache.objects.filter(projet_id = project.id).order_by('-dateFin')[0]
                    project.dateLivraison = latest.dateFin
                    
                    # Associe automatiquement le statut du projet
                    project_tasks = Tache.objects.filter(projet_id = project.id)
                    is_Deliverable = True

                    for task in project_tasks:
                        if task.statut != 4:
                            is_Deliverable = False
                    if is_Deliverable:
                        project.statut = 3
                    elif project.dateLivraison <= timezone.now().date():
                        project.statut = 4
                    elif project_tasks.filter(statut__range=(0,3)).exists:
                        project.statut = project_tasks.filter(statut__range=(0,3)).order_by('-statut')[0].statut
                    else:
                        project.statut = 100

                except IndexError:
                    project.dateDebut = None
                    project.dateLivraison = None
                    project.statut = 0

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

# Les trois prochaines vues sont pour renvoyer tout les objets de chaque type dans la BDD
# ils sont aussi les cibles des redirection en cas de succès dans la soumissions d'un formulaire
def allusers(request):
    try:
        users = Utilisateur.objects.filter()
        data ={
            'users':[user.to_json() for user in users]
        }
        return JsonResponse(data)
    except:
        return JsonResponse({'error' : 'Something went wrong'})

def allprojects(request):
    try:
        projects = Projet.objects.filter()
        data ={
            'projects': [project.to_json() for project in projects]
        }
        return JsonResponse(data)
    except:
        return JsonResponse({'error' : 'Something went wrong'})
    
def alltasks(request):
    try:
        tasks = Tache.objects.filter()
        data ={
            'tasks': [task.to_json() for task in tasks]
        }
        return JsonResponse(data)
    except:
        return JsonResponse({'error' : 'Something went wrong'})

# Les vues gérant la logique de création des objets avec les formulaires
def createuser(request):
    if request.method == 'POST':
        form = FormulaireUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allusers')
    else:
        form = FormulaireUtilisateur()
    return render(request, 'createuser.html', {'form': form})

def createproject(request):
    if request.method == 'POST':
        form = FormulaireProjet(request.POST)
        if form.is_valid():
            form.save()
            return redirect('allprojects')
    else:
        form = FormulaireProjet()

    user_id = request.session.get('user_id')
    utilisateur = Utilisateur.objects.get(id=user_id)
    context = {'form': form, 'utilisateur': utilisateur}
    return render(request, 'createproject.html', context)

def createtask(request):
    if request.method == 'POST':
        form = FormulaireTache(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alltasks')
    else:
        form = FormulaireTache()
<<<<<<< HEAD
    return render(request, 'createtask.html', {'form': form})
=======

    user_id = request.session.get('user_id')
    utilisateur = Utilisateur.objects.get(id=user_id)
    context = {'form': form, 'utilisateur': utilisateur}
    return render(request, 'createtask.html', context)
>>>>>>> 62b58f7 (ajout cta)
