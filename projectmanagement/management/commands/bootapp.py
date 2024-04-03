from django.core.management.base import BaseCommand
from django.core.management import call_command
import sys

class Command(BaseCommand):
    help = 'Deletes all data, creates test data, and starts the development server with specified IP:port. Yes has to be selected twice'

    def add_arguments(self, parser):
        parser.add_argument('ip-port', type=str, help='The IP:port address to run the server on.')

    def handle(self, *args, **kwargs):
        # Supprime la totalité des données (ATTTENTION, IRREVERSIBLE)
        call_command('flush', interactive=False)
        # Appelle la commande 'testdata create', utilise le fichier testdata.py
        call_command('testdata', 'create')
        # Appelle la commande 'runserver ip:port'
        ip = kwargs['ip-port']
        # Known issue, ceci appelle le handle 2 fois à cause d'une erreur de multi-thread, ne pose pas problème car le bootapp n'est pas à utiliser en prod
        call_command('runserver', ip)