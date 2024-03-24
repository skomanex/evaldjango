from django.urls import path

from . import views

urlpatterns = [
    # http://192.168.56.12/projectmanagement/
    path("", views.index, name="index"),
    # http://192.168.56.12/projectmaangement/User1
    path('<str:utilisateur>', views.pageutilisateur, name="pageutilisateur")
]
