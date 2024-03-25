# projectmanagement/management/commands/apptask.py
# ce fichier permet l'administration' d'un Tache à l'aide de la commande python3 manage.py apptask

from django.core.management.base import BaseCommand
from projectmanagement.models import Tache
from projectmanagement.forms import FormulaireTache

class Command(BaseCommand):
    help = 'Manage tasks with arguments create, modify or delete. Can only manage one task at a time and should only be used to setup the first one'

    # Ajout des différents arguments de la commande (create, modify, delete)
    def add_arguments(self, parser):
        parser.add_argument('option', choices=['create', 'modify', 'delete'])

    def handle(self, *args, **kwargs):

        option = kwargs['option']

        if option == 'create':

            # Option 'create' entrée avec la commande, on créer un nouveau formulaire
            form = FormulaireTache()
            task_data = {}
            
            # Prompte l'utilisateur de remplir tout les champs
            for field in form.fields:
                task_data[field] = input(f"Please enter task's {field} : ")
            
            # On vient lier un formulaire pour pouvoir l'utiliser pour sauvegarder un nouvel Tache
            new_task = FormulaireTache(data = task_data)
            
            # Vérification native Django de la vérification de formulaire
            if new_task.is_valid():
                new_task.save()
                self.stdout.write(self.style.SUCCESS('task created successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to create task. Please check your input.'))
                for field, errors in new_task.errors.items():
                    self.stdout.write(self.style.ERROR(f"{field}: {', '.join(errors)}"))
        
        # On arrive jusqu'ici si l'option create n'a pas été choisie, on définit donc les fonction pour trouver un Tache
        # qui seront utilisée dans modify et delete
        # Trouve l'Tache par nom
        def find_task_by_name(name):
            try:
                task = Tache.objects.get(nom=name)
                return task
            except Tache.DoesNotExist:
                print(f"No task found with name '{name}'")
                return None

        #Trouve l'Tache par id
        def find_task_by_id(task_id):
            try:
                task = Tache.objects.get(id=task_id)
                return task
            except Tache.DoesNotExist:
                print(f"No task found with ID '{task_id}'")
                return None

        # Met à jour les champs
        def update_task_fields(task):
            # Utilise la même façon que pour la création , mais on spécifie une instance à la liason du formulaire pour mettre à jour les champs de cette instance.
            form = FormulaireTache()
            task_data = {}
            for field in form.fields:
                task_data[field] = input(f"Please enter task's new {field} : ")
            task_form = FormulaireTache(data = task_data, instance = task)
            if task_form.is_valid():
                task_form.save()
                self.stdout.write(self.style.SUCCESS('task updated successfully!'))
            else:
                self.stdout.write(self.style.ERROR('Failed to update task. Please check your input.'))
                for field, errors in task_form.errors.items():
                    self.stdout.write(self.style.ERROR(f"{field}: {', '.join(errors)}"))

        # Option modifier, on change les champs si on trouve l'Tache
        if option == 'modify':
            search = input(f"Find task by? (id, name)\n").lower()

            if search == 'name':
                name = input("Enter task's name: ")
                task = find_task_by_name(name)
            elif search == 'id':
                task_id = input("Enter task's ID: ")
                task = find_task_by_id(task_id)
            else:
                print("Invalid search option. Please choose 'name', 'id', or 'email'.")
                return
        
            # Si l'Tache est trouvé
            if task:
                update_task_fields(task)
        
        # Option supprimer, on supprime l'Tache
        if option == 'delete':
            search = input(f"Find task by? (id, name)\n").lower()

            if search == 'name':
                name = input("Enter task's name: ")
                task = find_task_by_name(name)
            elif search == 'id':
                task_id = input("Enter task's ID: ")
                task = find_task_by_id(task_id)
            else:
                print("Invalid search option. Please choose 'name', 'id', or 'email'.")
                return
        
            # Si l'Tache est trouvé
            if task:
                task.delete()
