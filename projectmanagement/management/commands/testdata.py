# projectmanagement/management/commands/testdata.py
# utiliser avec manage.py tesdata create ou manage.py testdata delete

from django.core.management.base import BaseCommand
from projectmanagement.models import Utilisateur, Projet, Tache
from projectmanagement.management.test_data import users_data, projects_data, tasks_data
from random import choice, randrange

class Command(BaseCommand):
    help = 'Manages test data, create data contained in test_data.py using argument create or destroy all data flagged with estTest with argument delete'

    def add_arguments(self, parser):
        parser.add_argument('option', choices=['create', 'delete'])

    def handle(self, *args, **kwargs):

        option = kwargs['option']

        if option == 'create':
            # Créer les utilisateurs définis dans fake_data.py
            for user_data in users_data:
                # Créer les utilisateurs si il n'existe pas
                if not Utilisateur.objects.filter(**user_data).exists():
                    Utilisateur.objects.create(**user_data)

            # Créer les projets définis dans fake_data.py
            for project_data in projects_data:
                # Créer les projets si ils n'existent pas
                if not Projet.objects.filter(**project_data).exists():
                    # Choisis un responsable au hasard parmis les disponibles
                    manager = choice(Utilisateur.objects.filter(estResponsable = True))
                    project_data['responsable_id'] = manager.id
                    Projet.objects.create(**project_data)

            # Créer les tâches définies dans fake_data.py          
            for task_data in tasks_data:
                # Créer les tâches si elles n'existent pas
                if not Tache.objects.filter(**task_data).exists():
                    # Choisis un projet au hasard parmis les disponibles
                    project = choice(Projet.objects.all())
                    task_data['projet_id'] = project.id
                    Tache.objects.create(**task_data)

            for task in Tache.objects.all():
                for i in range(0, randrange(1, len(users_data)+1)):
                    task.executant.add(Utilisateur.objects.get(nom = users_data[i].get('nom')))
            self.stdout.write(self.style.SUCCESS('Data created successfully'))

        elif option == 'delete':
            # Supprime les objets Utilisateur avec estTest = True
            Utilisateur.objects.filter(estTest=True).delete()
            # Supprime les objets Projet avec estTest = True
            Projet.objects.filter(estTest=True).delete()
            # Supprime les objets Taches avec estTest = True
            Tache.objects.filter(estTest=True).delete()
            self.stdout.write(self.style.SUCCESS('Test data flagged with estTest = True deleted successfully'))
