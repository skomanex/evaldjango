# projectmanagement/management/commands/createappuser.py
# ce fichier permet la création d'un utilisateur à l'aide de la commande python3 manage.py createappuser

from django.core.management.base import BaseCommand
from projectmanagement.models import Utilisateur
from projectmanagement.forms import FormulaireUtilisateur

class Command(BaseCommand):
    help = 'Manage users with arguments create, modify or delete. Can only manage one user at a time and should only be used to setup the first one'

    # Ajout des différents arguments de la commande (create, modify, delete)
    def add_arguments(self, parser):
        parser.add_argument('option', choices=['create', 'modify', 'delete'])

    def handle(self, *args, **kwargs):

        option = kwargs['option']

        if option == 'create':

            # Option 'create' entrée avec la commande, on créer un nouveau formulaire
            form = FormulaireUtilisateur()
            user_data = {}
            
            # Prompte l'utilisateur de remplir tout les champs
            for field in form.fields:
                user_data[field] = input(f"Please enter user's {field} : ")
            
            # On vient lier un formulaire pour pouvoir l'utiliser pour sauvegarder un nouvel utilisateur
            new_user = FormulaireUtilisateur(data = user_data)
            
            # Vérification native Django de la vérification de formulaire
            if new_user.is_valid():
                new_user.save()
                self.stdout.write(self.style.SUCCESS('User created successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to create user. Please check your input.'))
                for field, errors in new_user.errors.items():
                    self.stdout.write(self.style.ERROR(f"{field}: {', '.join(errors)}"))
        
        # On arrive jusqu'ici si l'option create n'a pas été choisie, on définit donc les fonction pour trouver un utilisateur
        # qui seront utilisée dans modify et delete
        # Trouve l'utilisateur par nom
        def find_user_by_name(name):
            try:
                user = Utilisateur.objects.get(nom=name)
                return user
            except Utilisateur.DoesNotExist:
                print(f"No user found with name '{name}'")
                return None

        #Trouve l'utilisateur par id
        def find_user_by_id(user_id):
            try:
                user = Utilisateur.objects.get(id=user_id)
                return user
            except Utilisateur.DoesNotExist:
                print(f"No user found with ID '{user_id}'")
                return None

        #Trouve l'utilisteur par email
        def find_user_by_email(email):
            try:
                user = Utilisateur.objects.get(mail=email)
                return user
            except Utilisateur.DoesNotExist:
                print(f"No user found with email '{email}'")
                return None
        
        # Met à jour les champs
        def update_user_fields(user):
            new_nom = input("Enter new name: ")
            new_mdp = input("Enter new password: ")
            new_mail = input("Enter new email: ")
            new_estResponsable = input("Is the user responsible? (True/False): ").lower() == 'true'

            user.nom = new_nom
            user.mdp = new_mdp
            user.mail = new_mail
            user.estResponsable = new_estResponsable
            user.save()

        # Option modifier, on change les champs si on trouve l'utilisateur
        if option == 'modify':
            search = input(f"Find user by? (id, name, email)\n").lower()

            if search == 'name':
                name = input("Enter user's name: ")
                user = find_user_by_name(name)
            elif search == 'id':
                user_id = input("Enter user's ID: ")
                user = find_user_by_id(user_id)
            elif search  == 'email':
                email = input("Enter user's email: ")
                user = find_user_by_email(email)
            else:
                print("Invalid search option. Please choose 'name', 'id', or 'email'.")
                return
        
            # Si l'utilisateur est trouvé
            if user:
                update_user_fields(user)
        
        # Option supprimer, on supprime l'utilisateur
        if option == 'delete':
            search = input(f"Find user by? (id, name, email)\n").lower()

            if search == 'name':
                name = input("Enter user's name: ")
                user = find_user_by_name(name)
            elif search == 'id':
                user_id = input("Enter user's ID: ")
                user = find_user_by_id(user_id)
            elif search  == 'email':
                email = input("Enter user's email: ")
                user = find_user_by_email(email)
            else:
                print("Invalid search option. Please choose 'name', 'id', or 'email'.")
                return
        
            # Si l'utilisateur est trouvé
            if user:
                user.delete()
