# projectmanagement/management/commands/createfakedata.py
# ce fichier permet la création des tâches à partir de la commande "python3 manage.py creatrefakedata"

from django.core.management.base import BaseCommand
from projectmanagement.models import Utilisateur, Projet, Tache
from projectmanagement.management.fake_data import users_data, projects_data, tasks_data
from random import choice

class Command(BaseCommand):
    help = 'Creates some example data to test the features'

    def handle(self, *args, **kwargs):

        # Créer les utilisateurs définis dans fake_data.py
        if not Utilisateur.objects.exists():
            # Créer les utilisateurs si il n'existe pas
            for user_data in users_data:
                Utilisateur.objects.create(**user_data)

        # Filtre pour ne garder que ceux définis comme "responsable"
        responsables = Utilisateur.objects.filter(estResponsable=True)

        # Si il n'y a pas de responsable retourne une erreur (ne devrait jamais arriver par défaut car génère en utilisant fake_data.py qui en contient au moins un (sauf modification))
        if not responsables.exists():
            self.stdout.write(self.style.ERROR('No responsible users found. Aborting project creation.'))
            return

        # Créer les projets définis dans fake_data.py
        if not Projet.objects.exists():
            # Créer les projets si ils n'existent pas
            for project_data in projects_data:
                responsable = choice(responsables)
                project_data['responsable_id'] = responsable.id
                Projet.objects.create(**project_data)

        # Créer les tâches définies dans fake_data.py
        # Si il n'y a pas de projets retourne une erreur (ne devrait jamais arriver par défaut car génère en utilisant fake_data.py qui en contient au moins un (sauf modification))
        if not Projet.objects.exists():
            self.stdout.write(self.style.ERROR('No project found. Aborting Task creation.'))
            return
        
        if not Tache.objects.exists():
            # Créer les tâches si elles n'existent pas
            for task_data in tasks_data:
                projet = choice(Projet.objects.all())
                task_data['projet_id'] = projet.id
                Tache.objects.create(**task_data)

        self.stdout.write(self.style.SUCCESS('Data created successfully, you can check on the /admin page with a django superuser login'))
