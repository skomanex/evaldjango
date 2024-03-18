# projectmanagement/management/commands/deletefakedata.py

from django.core.management.base import BaseCommand
from projectmanagement.models import Utilisateur, Projet, Tache

class Command(BaseCommand):
    help = 'Deletes all objects with flagged with estTest as True'

    def handle(self, *args, **kwargs):
        # Supprime les objets Utilisateur avec estTest = True
        Utilisateur.objects.filter(estTest=True).delete()
        # Supprime les objets Projet avec estTest = True
        Projet.objects.filter(estTest=True).delete()
        # Supprime les objets Taches avec estTest = True
        Tache.objects.filter(estTest=True).delete()

        self.stdout.write(self.style.SUCCESS('Fake data flagged with estTest = True deleted successfully'))
