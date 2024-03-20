# projectmanagement/management/commands/createappuser.py
# ce fichier permet la création d'un utilisateur à l'aide de la commande python3 manage.py createappuser

from django.core.management.base import BaseCommand
from projectmanagement.forms import FormulaireUtilisateur

class Command(BaseCommand):
    help = 'Creates a user that will be able to log in to the app'

    def handle(self, *args, **kwargs):
        form = FormulaireUtilisateur()
        user_data = {}

        for field in form.fields:
            user_data[field] = input(f"Please enter user's {field} : ")
        new_user = FormulaireUtilisateur(data = user_data)
        if new_user.is_valid():
            new_user.save()
            self.stdout.write(self.style.SUCCESS('User created successfully!'))
        else:
            self.stdout.write(self.style.ERROR('Failed to create user. Please check your input.'))
            for field, errors in new_user.errors.items():
                self.stdout.write(self.style.ERROR(f"{field}: {', '.join(errors)}"))