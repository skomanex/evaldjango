from django.db import models
from django.utils import timezone

# Create your models here.
class Utilisateur(models.Model):
    nom = models.CharField(max_length=200)
    mdp = models.TextField(max_length=255)
    mail = models.EmailField()
    estResponsable = models.BooleanField(default=False)
    estTest = models.BooleanField(default = False)

    def __str__(self):
        return self.nom
    
    def to_json(self):
        data = {
            'nom': self.nom,
            'mail': self.mail,
            'estResponsable': self.estResponsable
        }
        return data


class Projet(models.Model):
    nom = models.CharField(max_length=40)
    responsable = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    statut = models.IntegerField(default = 3)
    statutVerbose = models.CharField(max_length = 40, default = "en pause")
    dateDebut = models.DateField(null =  True, blank = True)  
    dateLivraison = models.DateField(null = True, blank = True)
    estTest = models.BooleanField(default = False)
    
    @property
    def avancementSuppose(self):
        if (self.dateDebut is not None) and (self.dateLivraison is not None):
            total_time = (self.dateLivraison - self.dateDebut).days
            current_time = (timezone.now().date() - self.dateDebut).days
            return min(current_time/total_time, 1)
        else:            
            return 0

    def __str__(self):
        return self.nom
    
    def to_json(self):
        data = {
            'nom': self.nom,
            'statut': self.statut,
            'statutVerbose': self.statutVerbose,
            'responsableId': self.responsable.id,
            'responsableNom': self.responsable.nom,
            'dateDebut': self.dateDebut,
            'dateLivraison': self.dateLivraison,
            'avancementSuppose': self.avancementSuppose
        }
        return data


class Tache(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    projet = models.ForeignKey(Projet, on_delete=models.CASCADE)
    priorite = models.IntegerField()
    dateDebut = models.DateField()
    dateFin = models.DateField()
    statut = models.IntegerField()
    executant = models.ManyToManyField(Utilisateur)
    tacheParent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    rapportAvancement = models.TextField(blank=True)
    estTest = models.BooleanField(default = False)

    # Définition d'un statut verbose accessible comme une propriété
    @property
    def statutVerbose(self):
        if self.statut == 0:
            return "planifiée"
        elif self.statut == 1:
            return "en cours"
        elif self.statut == 2:
            return "réalisée"
        elif self.statut == 3:
            return "validée"
        elif self.statut == 4:
            return "en pause"
        else:
            return "erreur"

    def __str__(self):
        return self.nom
    
    def parentExiste(self):
        if self.tacheParent is None:
            return "null"
        else:
            return self.tacheParent.id

    def to_json(self):
        data = {
            'nom': self.nom,
            'description': self.description,
            'projetId': self.projet.id,
            'projetNom': self.projet.nom,
            'tacheParentId': self.parentExiste(),
            'priorite': self.priorite,
            'statut': self.statut,
            'statutVerbose' : self.statutVerbose,
            'dateDebut': self.dateDebut,
            'dateFin': self.dateFin
        }
        return data
