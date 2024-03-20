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