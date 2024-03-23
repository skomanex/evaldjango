from django.db import models


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
    statut = models.IntegerField()
    dateLivraison = models.DateField()
    responsable = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    dateDebut = models.DateField()
    avancementEffectif = models.FloatField()
    avancementSuppose = models.FloatField()
    estTest = models.BooleanField(default = False)

    def __str__(self):
        return self.nom
    
    def to_json(self):
        data = {
            'nom': self.nom,
            'statut': self.statut,
            'responsableId': self.responsable.id,
            'responsableNom': self.responsable.nom,
            'dateDebut': self.dateDebut,
            'dateLivraison': self.dateLivraison,
            'avancementEffectif': self.avancementEffectif
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
    avancement = models.FloatField()
    estTest = models.BooleanField(default = False)

    def __str__(self):
        return self.nom
    
    def to_json(self):
        data = {
            'nom': self.nom,
            'description': self.description,
            'projetId': self.projet.id,
            'projetNom': self.projet.nom,
            'priorite': self.priorite,
            'statut': self.statut,
            'dateDebut': self.dateDebut,
            'dateFin': self.dateFin,
            'avancement': self.avancement
        }
        return data
