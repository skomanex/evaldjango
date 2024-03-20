from django.forms import ModelForm
from projectmanagement.models import Utilisateur, Tache, Projet

class FormulaireUtilisateur(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['nom', 'mdp', 'mail', 'estResponsable', 'estTest']


class FormulaireTache(ModelForm):
    class Meta:
        model = Tache
        fields = ['nom', 'description', 'projet', 'priorite', 'dateDebut', 'dateFin', 'statut', 'executant',
                  'tacheParent', 'rapportAvancement', 'avancement']

class FormulaireProjet(ModelForm):
    class Meta:
        model = Projet
        fields = ['nom', 'statut', 'dateLivraison', 'responsable', 'dateDebut']