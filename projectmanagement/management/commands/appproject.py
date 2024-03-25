# projectmanagement/management/commands/appproject.py
# ce fichier permet l'administration' d'un Projet à l'aide de la commande python3 manage.py appproject

from django.core.management.base import BaseCommand
from projectmanagement.models import Projet
from projectmanagement.forms import FormulaireProjet

class Command(BaseCommand):
    help = 'Manage projects with arguments create, modify or delete. Can only manage one project at a time and should only be used to setup the first one'

    # Ajout des différents arguments de la commande (create, modify, delete)
    def add_arguments(self, parser):
        parser.add_argument('option', choices=['create', 'modify', 'delete'])

    def handle(self, *args, **kwargs):

        option = kwargs['option']

        if option == 'create':

            # Option 'create' entrée avec la commande, on créer un nouveau formulaire
            form = FormulaireProjet()
            project_data = {}
            
            # Prompte l'utilisateur de remplir tout les champs
            for field in form.fields:
                project_data[field] = input(f"Please enter project's {field} : ")
            
            # On vient lier un formulaire pour pouvoir l'utiliser pour sauvegarder un nouvel Projet
            new_project = FormulaireProjet(data = project_data)
            
            # Vérification native Django de la vérification de formulaire
            if new_project.is_valid():
                new_project.save()
                self.stdout.write(self.style.SUCCESS('project created successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to create project. Please check your input.'))
                for field, errors in new_project.errors.items():
                    self.stdout.write(self.style.ERROR(f"{field}: {', '.join(errors)}"))
        
        # On arrive jusqu'ici si l'option create n'a pas été choisie, on définit donc les fonction pour trouver un Projet
        # qui seront utilisée dans modify et delete
        # Trouve l'Projet par nom
        def find_project_by_name(name):
            try:
                project = Projet.objects.get(nom=name)
                return project
            except Projet.DoesNotExist:
                print(f"No project found with name '{name}'")
                return None

        #Trouve l'Projet par id
        def find_project_by_id(project_id):
            try:
                project = Projet.objects.get(id=project_id)
                return project
            except Projet.DoesNotExist:
                print(f"No project found with ID '{project_id}'")
                return None

        # Met à jour les champs
        def update_project_fields(project):
            # Utilise la même façon que pour la création , mais on spécifie une instance à la liason du formulaire pour mettre à jour les champs de cette instance.
            form = FormulaireProjet()
            project_data = {}
            for field in form.fields:
                project_data[field] = input(f"Please enter project's new {field} : ")
            project_form = FormulaireProjet(data = project_data, instance = project)
            if project_form.is_valid():
                project_form.save()
                self.stdout.write(self.style.SUCCESS('project updated successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to update project. Please check your input.'))
                for field, errors in project_form.errors.items():
                    self.stdout.write(self.style.ERROR(f"{field}: {', '.join(errors)}"))

        # Option modifier, on change les champs si on trouve l'Projet
        if option == 'modify':
            search = input(f"Find project by? (id, name)\n").lower()

            if search == 'name':
                name = input("Enter project's name: ")
                project = find_project_by_name(name)
            elif search == 'id':
                project_id = input("Enter project's ID: ")
                project = find_project_by_id(project_id)
            else:
                print("Invalid search option. Please choose 'name', 'id', or 'email'.")
                return
        
            # Si l'Projet est trouvé
            if project:
                update_project_fields(project)
        
        # Option supprimer, on supprime l'Projet
        if option == 'delete':
            search = input(f"Find project by? (id, name)\n").lower()

            if search == 'name':
                name = input("Enter project's name: ")
                project = find_project_by_name(name)
            elif search == 'id':
                project_id = input("Enter project's ID: ")
                project = find_project_by_id(project_id)
            else:
                print("Invalid search option. Please choose 'name', 'id', or 'email'.")
                return
        
            # Si l'Projet est trouvé
            if project:
                project.delete()
