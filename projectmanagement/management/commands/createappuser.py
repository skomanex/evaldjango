# projectmanagement/management/commands/createappuser.py
# ce fichier permet la création d'un utilisateur à l'aide de la commande python3 manage.py createappuser

from django.core.management.base import BaseCommand
from projectmanagement.models import Utilisateur

class Command(BaseCommand):
    help = 'Creates an user that will be able to login in the app'

    def handle(self, *args, **kwargs):
        for attribut in Utilisateur._meta.fields:
            self.stdout.write(self.style.SUCCESS(f'PLease enter user\'s {attribut}'))
