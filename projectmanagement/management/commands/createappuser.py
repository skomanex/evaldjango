# projectmanagement/management/commands/createappuser.py
# ce fichier permet la création d'un utilisateur à l'aide de la commande python3 manage.py createappuser

from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from projectmanagement.forms import FormulaireUtilisateur

class Command(BaseCommand):
    help = 'Creates a user that will be able to log in to the app'

    def handle(self, *args, **kwargs):
        form = FormulaireUtilisateur()
        for field in form.fields:
            user_input = input(f"Please enter user's {field}: ")
            form.data[field] = user_input
        print(form.is_bound)
        if form.is_valid():
            form.save()
            self.stdout.write(self.style.SUCCESS('User created successfully!'))
        else:
            print(form.errors.as_json())
            print(form.is_valid())
