from django.contrib import admin

# Register your models here.

from .models import Utilisateur
from .models import Projet
from .models import Tache

admin.site.register(Utilisateur)
admin.site.register(Projet)
admin.site.register(Tache)
