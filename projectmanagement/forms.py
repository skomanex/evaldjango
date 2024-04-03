from django.forms import ModelForm
from projectmanagement.models import Utilisateur, Tache, Projet

class FormulaireUtilisateur(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'mdp', 'mail', 'estResponsable', 'estTest']
        labels = {
            'nom': 'Nom de l\'utilisateur',
            'mdp': 'Mot de passe',
            'mail': 'Email',
            'estResponsable': 'Responsable',
            'estTest': 'Est un test',
        }


class FormulaireTache(ModelForm):
    class Meta:
        model = Tache
        fields = ['nom', 'description', 'projet', 'priorite', 'dateDebut', 'dateFin', 'statut', 'executant',
                  'tacheParent', 'rapportAvancement', 'estTest']
        labels = {
            'nom': 'Nom de la tâche',
            'description': 'Description de la tâche',
            'projet': 'Projet associé',
            'priorite': 'Priorité de la tâche',
            'dateDebut': 'Date de début',
            'dateFin': 'Date de fin',
            'statut': 'Statut de la tâche',
            'executant': 'Executant de la tâche',
            'tacheParent': 'Tâche parente',
            'rapportAvancement': 'Rapport d\'avancement',
            'estTest': 'Est un test',
        }

class FormulaireProjet(ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'responsable', 'estTest']
        labels = {
            'nom': 'Nom du projet',
            'responsable': 'Responsable du projet',
        }